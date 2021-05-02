from threading import Lock
from flask import Flask, render_template, request, session, redirect, url_for, g
from flask_socketio import SocketIO, emit, disconnect
from recog import Recogniser
from recog import MaskRecogniser
from flask_mysqldb import MySQL
import cv2

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'studentrecog'



def background_thread():
    state = 0
    found_student_id = -1
    found_confidence = -1
    socketio.emit('state_change', { 'new_state':  'face' })
    cam = cv2.VideoCapture(0)
    r = Recogniser()
    m = MaskRecogniser()
    m.set_camera(cam)
    r.set_camera(cam)

    while True:
        socketio.sleep(0.03)
        if(state == 0):
            r1, r2, image = r.get_student_id()
            socketio.emit('image_data', { 'buffer':  'data:image/jpg;base64,'+image, 'student_id' : r1, 'confidence' : r2})
            if(r2 < 90) and (r2 != -1 and r1 != -1):
                print("Found Student ID: " + str(r1))
                found_student_id = r1
                found_confidence = r2
                state = 1
                socketio.emit('state_change', { 'new_state':  'mask' })
        elif(state == 1):
           _, r2, image = m.get_mask()
           socketio.emit('image_data', { 'buffer': 'data:image/jpg;base64,'+image, 'student_id' : found_student_id, 'confidence' : str(r2)})
           if(r2 >= 0.9999):
                state = 2
                socketio.emit('state_change', { 'new_state':  'update database' })
        elif(state == 2):
            #MAKE DATABASE REQUEST
            found_student_id = -1
            found_confidence = 0 
            state = 0
            socketio.emit('state_change', { 'new_state':  'face' })

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = 'username' #name of user needs to be taken from databse
        g.user = user

@app.route('/')
def blank():
    return redirect(url_for('login'))

@app.route('/lectures')
def index():
    if session.get('logged_in') == True:
        return render_template('Lectures.html')
    else:
        return redirect(url_for('login'))
        

@app.route('/homepage')
def homepage():
    if session.get('logged_in') == True:
        return render_template('Homepage.html')
    else:
        return redirect(url_for('login'))

@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student_info(First_Name, Last_Name) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('student.html')


@app.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        if username == 'username' and password == 'password':
            session['user_id'] = username
            session['logged_in'] = True

            return redirect(url_for('homepage'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('Login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app, debug=True)

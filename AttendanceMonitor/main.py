from threading import Lock
from flask import Flask, render_template, request,jsonify
from flask_socketio import SocketIO, emit, disconnect
from flask_restful import Resource, Api
from recog import Recogniser
import json


# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


def background_thread():
    state = 0
    found_student_id = -1
    found_confidence = -1
    socketio.emit('state_change', { 'new_state':  'face' })
    r = Recogniser()
    while True:
        socketio.sleep(0.03)
        if(state == 0):
            r1, r2, image = r.get_student_id()            
            socketio.emit('image_data', { 'buffer':  'data:image/jpg;base64,'+image, 'student_id' : r1, 'confidence' : r2})
            if(r2 < 90):
                found_student_id = r1
                found_confidence = r2
                state = 1
                socketio.emit('state_change', { 'new_state':  'mask' })
        elif(state == 1):
           found_student_id, r2, image = r.get_student_id()
           socketio.emit('image_data', { 'buffer': 'data:image/jpg;base64,'+image, 'student_id' : found_student_id, 'confidence' : r2})
           if(r2 > 99000):
                state = 2
                socketio.emit('state_change', { 'new_state':  'update database' })
        elif(state == 2):
           #MAKE DATABASE REQUEST
            found_student_id = -1
            found_confidence = 0 
            state = 0
            socketio.emit('state_change', { 'new_state':  'face' })

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class GetImage(Resource):
    def get(self):
        r= Recogniser()
        image = r.getImage()
        return {'image': image }



api.add_resource(GetImage, '/getimage')

#@app.route('/imagedata', methods=['GET'])
#def get_image():
 #  imgData = Recogniser.getImage()
  # return jsonify({'image': str(imgData)})

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

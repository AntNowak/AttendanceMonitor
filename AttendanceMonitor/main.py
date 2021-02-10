from flask import Flask, render_template, Response
from Recog import Recogniser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
def gen():
    recog = Recogniser()
    while True:
        student_id, confidence, image = recog.get_student_id()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n\r\n')

@app.route('/video_feed')   
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True) 
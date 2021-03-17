from flask import Flask, render_template, request,jsonify
from flask_restful import Resource, Api
from recog import Recogniser
import json

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'secret!'


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class GetImage(Resource):
    def get(self):
        r = Recogniser(False)
        student_id, confidence, image = r.get_student_id()
        return {'image': image, 'student_id': student_id, 'confidence': confidence}

api.add_resource(GetImage, '/getimage')

class GetMask(Resource):
    def get(self):
        r = Recogniser(True)
        result, confidence, image = r.get_student_id()
        return {'image': image, 'is_masked': result, 'confidence': confidence}

api.add_resource(GetMask, '/getmask')

if __name__ == '__main__':
    app.run(debug=True)
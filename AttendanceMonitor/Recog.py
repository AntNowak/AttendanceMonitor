import cv2
import ImageUtils

class Recogniser:

    def __init__ (self):
        self.cam = cv2.VideoCapture(0)
        self.recogniser = cv2.face.LBPHFaceRecognizer_create()
        self.recogniser.read("student_train.yml")

    def __del__(self):
        self.cam.release()

    def get_student_id(self):
        ret, image = self.cam.read()
        if(not ret):
            print("FAILED TO GET IMAGE")
        image_grey, bounding_box = ImageUtils.crop_and_greyscale(image)
        if(not image_grey.size == 0):
            studentID, confidence = self.recogniser.predict(image_grey)
            (x, y, w, h) = bounding_box
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

            student_info = "Student ID: " + str(studentID) + " (" + str(confidence) + "%)"
            cv2.putText(image, student_info, (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            
            ret, jpeg = cv2.imencode('.jpg', image)
            return studentID, confidence, jpeg.tobytes()
        else:
            ret, jpeg = cv2.imencode('.jpg', image)
            return -1, -1, jpeg.tobytes()

#r = Recog()

#while True:
#    s, c, i = r.get_student_id()
#    cv2.imshow('video', i)
#    k = cv2.waitKey(30) & 0xff
#    if k == 27: # press 'ESC' to quit
#        break

#cv2.destroyAllWindows()
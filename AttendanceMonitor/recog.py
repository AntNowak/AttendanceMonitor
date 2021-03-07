import cv2
import image_utils
import base64

class Recogniser:

    def __init__ (self):
        self.cam = cv2.VideoCapture(0)
        self.recogniser = cv2.face.LBPHFaceRecognizer_create()
        self.recogniser.read("student_train.yml")
        self.image = ""
        #self.mask_recogniser.read("mask_train.yml")

    def __del__(self):
        self.cam.release()
    
    def setImage(self, img):
        self.image = img
    def getImage(self):
        return self.image

    def get_student_id(self):
        ret, image = self.cam.read()
        if(not ret):
            print("FAILED TO GET IMAGE")
        image_grey, bounding_box = image_utils.crop_and_greyscale(image)
        if(not image_grey.size == 0):
            studentID, confidence = self.recogniser.predict(image_grey)
            #is_mask, confidence = self.mask_recogniser.predict(image_grey)
            (x, y, w, h) = bounding_box
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

            student_info = "Student ID: " + str(studentID) + " (" + str(confidence) + "%)"
            cv2.putText(image, student_info, (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            
            ret, image = cv2.imencode('.jpg', image)
            data = base64.b64encode(image).decode("UTF-8")
            setImage(data)
            return studentID, confidence, data
        else:
            ret, image = cv2.imencode('.jpg', image)
            data = base64.b64encode(image).decode("UTF-8")
            setImage(data)
            return -1, -1, data

#r = Recog()

#while True:
#    s, c, i = r.get_student_id()
#    cv2.imshow('video', i)
#    k = cv2.waitKey(30) & 0xff
#    if k == 27: # press 'ESC' to quit
#        break

#cv2.destroyAllWindows()

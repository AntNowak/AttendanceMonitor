
import cv2
import random
import numpy as np
from os import path, mkdir, listdir
CASCADE_PATH = "haarcascade_frontalface_default.xml"

def create_student_dir(student_id):
    user_data_dir = "user_data"
    if (not path.exists(user_data_dir)):
        mkdir(user_data_dir)
    user_dir = user_data_dir + "/" + student_id

    if (not path.exists(user_dir)):
        mkdir(user_dir)

    return user_dir


def crop_image(image, dir_name):
    cascade_class = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #change to greyscale
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #detecting faces
    faces = cascade_class.detectMultiScale(image_grey, 1.3, 5)
    print (len(faces))
    #creating rectangle
    for (x, y, w, h) in faces:
        crop_image = image[y: y + h, x: x + w]
        crop_image = cv2.resize(crop_image, (200, 200))
        cv2.imwrite(dir_name + "/" + str(random.randint(0,50000))+ ".jpg", crop_image)


def run_training():
    user_data_dir = "user_data"
    #finding user image directories
    user_dirs = listdir(user_data_dir)
    images = []
    ids = []
    #interate the student IDs
    for u in user_dirs:
        user_files = listdir(user_data_dir + "/" + u)
        #interating student images for IDs
        for f in user_files:
            image = cv2.imread(user_data_dir + "/" + u + "/" + f)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            ids.append(int(u))
            print (u)
            print (f)
            images.append(image)
    recogniser = cv2.face.LBPHFaceRecognizer_create()
    recogniser.train(images, np.array(ids))
    recogniser.write("student_train.yml")
        
def recognise_from_image(image):
    recogniser = cv2.face.LBPHFaceRecognizer_create()
    recogniser.read("student_train.yml") 


    cascade_class = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #detecting face
    faces = cascade_class.detectMultiScale(image, 1.3, 5)
    #creating rectangle
    for (x, y, w, h) in faces:
        image_grey = cv2.cvtColor(image[y: y + h, x: x + w], cv2.COLOR_BGR2GRAY)
        image_grey = cv2.resize(image_grey, (200, 200))
        id, confidence = recogniser.predict(image_grey)
        print (confidence)
        print (id)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)
        student_info = "Student ID: " + str(id) + " (" + str(confidence) + "%)"
        #display text
        if (confidence > 0):
            cv2.putText(image, student_info, (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        #show image
        cv2.imshow("image", image)
    cv2.waitKey()

def recognise_from_video():
    recogniser = cv2.face.LBPHFaceRecognizer_create()
    recogniser.read("student_train.yml") 
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
            image_grey = cv2.cvtColor(frame[y: y + h, x: x + w], cv2.COLOR_BGR2GRAY)
            image_grey = cv2.resize(image_grey, (200, 200))
            id, confidence = recogniser.predict(image_grey)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            student_info = "Student ID: " + str(id) + " (" + str(confidence) + "%)"
        #display text
            if (confidence > 0):
                cv2.putText(frame, student_info, (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        # display
        cv2.imshow('frame', frame)

        # esc to stop
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
    cap.release()
    cv2.destroyAllWindows()

#a = create_student_dir("89")   
#b = create_student_dir("90")

#for i in range(1,11):
#    image = cv2.imread("h" + str(i) + ".jpg")
 #   print ("h" + str(i) + ".jpg")
  #  crop_image(image, a)

#for i in range(1,11):
  #  image = cv2.imread("b" + str(i) + ".jpg")
  #  print (i)
   # crop_image(image, b)


#run_training()
image = cv2.imread("bh2.jpg")
#recognise_from_image(image)
recognise_from_video()
cv2.destroyAllWindows()





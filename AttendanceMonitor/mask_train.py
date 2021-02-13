
import cv2
import random
import ImageUtils
import numpy as np
from os import path, mkdir, listdir

class MaskTrain:

    def __init__ (self):
        self.cam = cv2.VideoCapture(0)

    def __del__(self):
        self.cam.release()

    def create_student_dir(self, student_id):
        user_data_dir = "user_data"
        if (not path.exists(user_data_dir)):
            mkdir(user_data_dir)
        user_dir = user_data_dir + "/" + student_id
        if (not path.exists(user_dir)):
            mkdir(user_dir)
        return user_dir

    def run_training(self):
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
                images.append(image)
        recogniser = cv2.face.LBPHFaceRecognizer_create()
        recogniser.train(images, np.array(ids))
        recogniser.write("mask_train.yml")


    def generate_training_set(self, student_id):
        student_dir = self.create_student_dir(student_id)
        number_of_images = 30
        saved_images = 0
        current_frame = 0

        while saved_images < number_of_images:
            ret, image = self.cam.read()
            if(current_frame % 10 == 0):
                if(not ret):
                    return False
                image, bounding_box = ImageUtils.crop_and_greyscale(image)
                if(not image.size == 0):
                    cv2.imwrite(student_dir + "/" + str(random.randint(0,50000))+ ".jpg", image)
                    saved_images += 1
            current_frame += 1

r = Train()
#r.generate_training_set("92")
r.run_training()



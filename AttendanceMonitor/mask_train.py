
import cv2
import random
import ImageUtils
import numpy as np
from os import path, mkdir, listdir

#https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset - masked dataset source
class MaskTrain:
    def run_training(self):
        mask_data_dir = "mask_data"
        masked_folder = "masked"
        unmasked_folder = "unmasked"

        #finding mask dataset directories
        mask_dirs = listdir(mask_data_dir + "/" + masked_folder)
        unmask_dirs = listdir(mask_data_dir + "/" + unmasked_folder)
        images = []
        ids = []

        #interate the masked data set
        for u in mask_dirs:
            user_files = listdir(mask_data_dir + "/" + masked_folder + "/" + u)
            for f in user_files:
                print(mask_data_dir + "/" + masked_folder + "/" + u + "/" + f)
                if('┼' in f):
                    continue
                image = cv2.imread(mask_data_dir + "/" + masked_folder + "/" + u + "/" + f)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                ids.append(1)
                images.append(image)

        #interate the unmasked data set
        for u in unmask_dirs:
            print(mask_data_dir + "/" + unmasked_folder + "/" + u)
            user_files = listdir(mask_data_dir + "/" + unmasked_folder + "/" + u)
            for f in user_files:
                print(mask_data_dir + "/" + unmasked_folder + "/" + u + "/" + f)
                image = cv2.imread(mask_data_dir + "/" + unmasked_folder + "/" + u + "/" + f)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                ids.append(0)
                images.append(image)

        recogniser = cv2.face.LBPHFaceRecognizer_create()
        recogniser.train(images, np.array(ids))
        recogniser.write("mask_train.yml")

r = MaskTrain()
r.run_training()



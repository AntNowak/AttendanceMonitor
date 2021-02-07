
import cv2

CASCADE_PATH = "haarcascade_frontalface_default.xml"

def crop_image(image):
    cascade_class = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #change to greyscale
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #detecting faces
    faces = cascade_class.detectMultiScale(image_grey, 1.3, 5)
    #creating rectangle
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)
    #show image
    cv2.imshow("image", image)
    cv2.waitKey()

    
image = cv2.imread("1.jpg")
crop_image(image)



cv2.destroyAllWindows()





#import the libraries
import cv2
import dlib
import face_recognition

#printing the versions
print(cv2.__version__)
print(dlib.__version__)
print(face_recognition.__version__)


image_test = cv2.imread("./images/testing/trump-modi.jpg")

cv2.imshow("Image", image_test)
import cv2 as cv
import numpy as np
img=cv.imread("images\lady.jpg")
#cv.imshow("lady",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("gray",gray)
haar_cascade = cv.CascadeClassifier('faces\haarcascade_frontalface_default.xml')#recognize the face
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)#returns list of faces cordinates
print("no of faces are:")
print(len(faces_rect))
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)
cv.waitKey(0)

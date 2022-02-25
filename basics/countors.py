from configparser import Interpolation
import cv2 as cv
import numpy as np
img = cv.imread("images/Modi.jpg")
img=cv.resize(img, (250,250), interpolation=cv.INTER_CUBIC)
cv.imshow("img",img)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("gray",gray)
ret,thresh=cv.threshold(gray,100,175,cv.THRESH_BINARY)
cv.imshow("thresh",thresh)
canny=cv.Canny(img,125,175)
#cv.imshow("canny",canny)
contours,heirchies=cv.findContours(thresh,cv.RETR_LIST ,cv.CHAIN_APPROX_SIMPLE)
#print((contours)) prints the coordinates of contours found
print(len(contours))
cv.waitKey(0)
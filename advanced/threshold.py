from multiprocessing.spawn import import_main_path


import cv2 as cv
import numpy as np
img=cv.imread("images/modi.jpg")
img=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#basic
threshold,thresh=cv.threshold(img,125,175,cv.THRESH_BINARY)
cv.imshow("thresh",thresh)
#inverse
threshold,thresh=cv.threshold(img,125,175,cv.THRESH_BINARY_INV)
cv.imshow("thresh_inv",thresh)
#adaptive
# thresh=cv.adaptiveThreshold(img,275,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,9)
# cv.imshow("thresh",thresh)
cv.imshow("img",img)
cv.waitKey(0)

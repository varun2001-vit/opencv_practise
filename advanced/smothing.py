import cv2 as cv
import numpy as np
img=cv.imread("images\loud.jpg")
cv.imshow("noice", img)
#averging
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)
#gaussian
gauss=cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blur', gauss)
# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)


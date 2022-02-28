import cv2 as cv
import numpy as np
img=cv.imread("images/dog.jpg")
blanks = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")
#cv.imshow("iamge",img)
#cv.imshow("blanks",blanks)
mask=cv.circle(blanks,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

cv.imshow("mask",mask)
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked",masked)
 











cv.waitKey(0)
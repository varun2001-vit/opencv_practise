import cv2 as cv
import numpy as np
blanks = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('blanks', blanks)
#drawing on the blanks
#blanks[100:300,200:400]=0,0,255
#cv.imshow('blanks', blanks)
#cv.waitKey(0)
#drawinf rectangle
# cv.rectangle(blanks,(0,0),(250,250),(0,250,0))
# cv.imshow('blanks_rectangle', blanks)
# cv.waitKey(0)
#drawing circle
# blanks1 = np.zeros((500,500,3),dtype='uint8')
# cv.circle(blanks1,(blanks1.shape[1]//2,blanks1.shape[0]//2),40,(0,250,250))
# cv.imshow('blanks_circle', blanks1)
# cv.waitKey(0)
# #drawing line
# blanks2 = np.zeros((500,500,3),dtype='uint8')
# cv.line(blanks2,(250,0),(250,250),(0,250,250))
# cv.imshow('blanks_line', blanks2)
# cv.waitKey(0)
#writing text 
cv.putText(blanks,"hi",(225,225),cv.FONT_HERSHEY_COMPLEX_SMALL,1.0,(0,225,225),2)
cv.imshow("text",blanks)
cv.waitKey(0)
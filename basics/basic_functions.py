import cv2 as cv
def rescale(frame ,scale=0.75):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dimesion = width,height
    return cv.resize(frame,dimesion,interpolation=cv.INTER_AREA)
img= cv.imread("images/Modi.jpg")
resized=rescale(img,scale=0.2)
#converting to gray scale
# gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
# cv.imshow("modi",resized)
# cv.imshow("modi_gray",gray)
# #blur
# blur=cv.GaussianBlur(resized,(11,11),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)
# #edgecascade
# canny=cv.Canny(resized,150,200)
# cv.imshow("edgecascade",canny)
# #dilating the images
# dialted=cv.dilate(canny,(7,7),iterations=3)
# cv.imshow("dilate",dialted)
# cv.waitKey(0)
# #eroding
# eroded=cv.erode(dialted,(7,7),iterations=3)
# cv.imshow("erode",eroded)
#resizing and cropping
re=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("resized",re);

#cropping
crop= img[20:50,200:500]
cv.imshow("cropped",crop)
cv.waitKey(0)

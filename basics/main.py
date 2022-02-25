import  cv2 as cv
#reading images
#img= cv.imread('images/dog.jpg')
#cv.imshow("dog",img);
#cv.waitKey(0);
#reading videos
capture=cv.VideoCapture(0) #capture vide
while True:  #untill video is runnig
    isTrue,frame=capture.read() #capturing frame
    flip=cv.flip(frame,1) #fl
    cv.imshow("video",flip);#displaiyng frame
    if( cv.waitKey(20) & 0xFF == ord('d')):#exit if d is presed
        break
capture.release()
cv.destroyAllWindows()

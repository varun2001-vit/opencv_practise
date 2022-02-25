import cv2 as cv
def rescale(frame ,scale=0.75):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dimesion = width,height
    return cv.resize(frame,dimesion,interpolation=cv.INTER_AREA)
capture=cv.VideoCapture(0) #capture vide
while True:  #untill video is runnig
    isTrue,frame=capture.read() #capturing frame
    frame_resized=rescale(frame)
    cv.imshow("video",frame)#displaiyng frame
    cv.imshow("video_resized",frame_resized)
    if( cv.waitKey(20) & 0xFF == ord('d')):#exit if d is presed
        break
capture.release()
cv.destroyAllWindows()
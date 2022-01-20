import cv2 as cv

#Reading videos
capture = cv.VideoCapture('Photos/lake2.jpg')
#in the case of reading videos, we use a while loop and read the video frame by frame
while True:
    isTrue, frame = capture.read() # reads video frame by frame and returns the frame and a boolean that says whether the frame was successfully read in or not
    cv.imshow('Video', frame) #display an individual frame
    
    if cv.waitKey(20) & 0xFF == ord('d'): #stop video from playing indefinitely
        #if the letter D is pressed, then break out of this loop and stop displaying the video
        break

capture.release() #release the capture pointer
cv.destroyAllWindows()
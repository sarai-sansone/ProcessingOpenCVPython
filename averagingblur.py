import cv2 as cv


img = cv.imread('Photos/lake2.jpg') 
cv.imshow('Image for Blur Function', img)

#Averaging
#blur is applied to the middle pixel as a result of the pixels around it, aka surrounding pixels
#we define a convolution matrix over a specific portion of an image. this will compute the pixel intensity of the middle pixel of the true center as the average of the surrounding pixel intensities
#the new pixel intensity of the middle pixel will be the average of all the surrounding pixel intensities
#this process happens throughout the image

average = cv.blur(img, (11,11)) #source, convolution matrix size
#the higher matrix size we specify, the more blur there is

cv.imshow('Average Blur', average)

cv.waitKey(0) 
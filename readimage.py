import cv2 as cv

#Reading images

img = cv.imread('Photos/lake2.jpg') #capture image in a variable called img

cv.imshow('Image To Read', img) #method displays the image as a new window, two parameters is name of window and matrix of pixels to display

cv.waitKey(0) #waits for a specific delay for a key to be pressed
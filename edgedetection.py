import cv2 as cv
import numpy as np

img = cv.imread('Photos/lake2.jpg') 
cv.imshow('Image for Edge Detection', img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

#Laplacian edges
lap = cv.Laplacian(grey, cv.CV_64F) #takes in source image and data depth
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)
cv.waitKey(0) 
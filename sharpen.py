import cv2 as cv
import numpy as np

img = cv.imread('Photos/lake2.jpg')

cv.imshow('Image', img)

sharpen_filter = np.array([[-1,-1,-1],
                            [-1,9,-1],
                            [-1,-1,-1]])

sharpened_img = cv.filter2D(img,-1,sharpen_filter)

cv.imshow('Sharpened Image', sharpened_img)

cv.waitKey(0)
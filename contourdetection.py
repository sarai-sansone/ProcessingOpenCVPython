import cv2 as cv

img = cv.imread('Photos/lake2.jpg') 
cv.imshow('Image for Contour Detection', img)

    #contours are the boundaries of objects
    #the lines/curves that joins the continuous points along the boundary of an object
    #contours and edges are different from each other
    #contours are useful for shape analysis and object detection and recognition

    #convert image to greyscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey',grey)

#blur = cv.GaussianBlur(grey, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

    #grab the edges of the image using the canny edge detector
#canny = cv.Canny(blur, 125, 175) #significant reduction of number of contours
canny = cv.Canny(img, 125, 175) #one possible method
cv.imshow('Canny Edges', canny)

    #threshold attepts to binarize an image: take an image and convert it into binary form
#ret, thresh = cv.threshold(grey, 125,255,cv.THRESH_BINARY) #another possible method 
    #125 as the threshold value, and 255 as the maximum value
#cv.imshow('Thresh',thresh)
    #find contours by using a method that returns contours and hierarchies

contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) #takes in the edges, a mode in which to find the contents, contour approximation method
#contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) 
    #RETR_LIST since we want all the contours in the image
    #RETR_TREE and RETR_EXTERNAL also possible
    #the contours is a Python list of all the coordinates of the contours that were found in the image
    #hierarchies refers to the hierarchial representation of contours

cv.waitKey(0) 
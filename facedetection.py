import cv2 as cv

img = cv.imread('Photos/people.jpg') 

cv.imshow('Image for Face Detection', img) 

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

#read in the XML file
#haar cascade variable
haar_cascade = cv.CascadeClassifier('haar_face.xml')
#CascadeClassifier will read in all those lines of code, and then store that in a variable

#detect face
faces_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=6) #pass in image, a scale factor
#minNeighbors specifices the number of neighbors a rectangle should have to be called a face
#faces_rect is the rectangular coordinates for the faces that are present in the image
#loop over list, grab coordinates, and draw a rectangle over the detected faces
print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (255,105,180), thickness=2) #draw rectangle over original image
    #image, point 1, point 2, rectangle color, thickness
cv.imshow('Detected Faces', img)
cv.waitKey(0)
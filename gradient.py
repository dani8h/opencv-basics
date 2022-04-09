import cv2 as cv
import numpy as np

img = cv.imread('photos\\flower.jpg')
img = cv.resize(img,(int(img.shape[1]*0.9),int(img.shape[0]*0.6)),interpolation = cv.INTER_AREA)
cv.imshow('flower',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)

#Sabel
#creates gradients in 2 directions

sobelx = cv.Sobel(gray, cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
#combined sobel
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('combinedsobel', combined_sobel)


#canny edge detector
canny = cv.Canny(gray,  150, 175)
cv.imshow('canny',canny)

cv.waitKey(0)
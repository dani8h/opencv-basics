import cv2 as cv
import numpy as np

img = cv.imread('photos\\nezuko.png')
img = cv.resize(img,(int(img.shape[1]*0.4),int(img.shape[0]*0.4)),interpolation = cv.INTER_AREA)
cv.imshow('nezuko',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank,(img.shape[1]//3,img.shape[0]//2),200,255,-1)
cv.imshow('mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)

cv.waitKey(0)
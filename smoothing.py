import cv2 as cv
import numpy as np

img = cv.imread('photos\\nezuko.png')
img = cv.resize(img,(int(img.shape[1]*0.4),int(img.shape[0]*0.4)),interpolation = cv.INTER_AREA)
cv.imshow('nezuko',img)


#Averaging
avg = cv.blur(img,(3,3)) #higher the kernel size more the blur
cv.imshow('average blur',avg)

#Gaussian blur
# instead of finding the average of surrounding pixels, it finds the product and then finds the average of the surrounding pixels
g = cv.GaussianBlur(img,(3,3),0)
cv.imshow('gaussian',g)

#Median blur
#helpful in removal of noise
median = cv.medianBlur(img,3)
cv.imshow('median',median)

#Bilateral
#most effective
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral blur', bilateral)



cv.waitKey(0)
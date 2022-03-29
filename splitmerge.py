import cv2 as cv
import numpy as np

img = cv.imread('photos\game.png')
img = cv.resize(img,(int(img.shape[1]*0.4),int(img.shape[0]*0.4)),interpolation = cv.INTER_AREA)
cv.imshow('naruto',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# splits the image into its respective components
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


merged = cv.merge([b,g,r])
cv.imshow('merged',merged)



cv.waitKey(0)
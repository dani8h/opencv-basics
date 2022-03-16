import cv2 as cv
import numpy as np 
img = cv.imread('photos\wp4789300-naruto-uzumaki-4k-wallpapers.jpg')

# #paint the image a certain color
# img[100:300, 200:280] = 0,233,40
# cv.imshow('Green',img)
# cv.waitKey(0)

# #draw a rectangle
# cv.rectangle(img,(0,0),(250,500),(0,255,0),thickness=2)
# cv.imshow('rectangle',img)
# cv.waitKey(0)

 #write text on a img
cv.putText(img,'Dattebayoo',(255,255),cv.FONT_HERSHEY_TRIPLEX,3.5,(0,210,190),2)
cv.imshow('text',img)
cv.waitKey(0)
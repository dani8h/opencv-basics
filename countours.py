import cv2 as cv
import numpy as np

img = cv.imread('photos\wp4789300-naruto-uzumaki-4k-wallpapers.jpg')
img = cv.resize(img,(int(img.shape[1]*0.22),int(img.shape[0]*0.22)),interpolation = cv.INTER_AREA)
cv.imshow('naruto',img)

#gray image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

canny = cv.Canny(img,125, 175)
cv.imshow('canny',canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#RETR_EXTERNAL returns all the external countours
#RETR_TREE returns all the heirarchial countours
#retr_list returns all the countours
print(len(contours))


#visualise the countours
#first create a blank 
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank',blank)

#now draw the contours on the blank
cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imshow('blank',blank)


cv.waitKey(0)
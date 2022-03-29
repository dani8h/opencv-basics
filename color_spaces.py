import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('photos\wp4789300-naruto-uzumaki-4k-wallpapers.jpg')
img = cv.resize(img,(int(img.shape[1]*0.22),int(img.shape[0]*0.22)),interpolation = cv.INTER_AREA)
cv.imshow('naruto',img)

#BGR to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)


#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#in other libararies such as matplotlib the color coding is RGB
plt.imshow(img)
plt.show()



cv.waitKey(0)
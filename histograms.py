import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos\\nezuko.png')
img = cv.resize(img,(int(img.shape[1]*0.4),int(img.shape[0]*0.4)),interpolation = cv.INTER_AREA)
cv.imshow('nezuko',img)

#grayscale histogram
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

gray_hist = cv.calcHist([gray],[0], None, [256],[0,256]) #params: list of images, index of image, mask, histsize:no of bins, range of all possible pixel values

plt.figure()
plt.title('grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
plt.plot(gray_hist)
plt.xlim(([0,256]))
plt.show()



#making a histogram only for a maks
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank,(img.shape[1]//3,img.shape[0]//2),200,255,-1)
cv.imshow('mask',mask)



cv.waitKey(0)
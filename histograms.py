import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos\\nezuko.png')
img = cv.resize(img,(int(img.shape[1]*0.4),int(img.shape[0]*0.4)),interpolation = cv.INTER_AREA)
cv.imshow('nezuko',img)

#grayscale histogram
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
plt.plot(gray_hist)
plt.xlim(([0,256]))
plt.show()


#making a histogram only for a mask
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//3,img.shape[0]//2),200,255,-1)

mask = cv.bitwise_and(gray, gray, mask = circle)
cv.imshow('mask',mask)

masked_hist = cv.calcHist([gray],[0], mask, [256],[0,256]) #params: list of images, index of image, mask, histsize:no of bins, range of all possible pixel values

plt.figure()
plt.title('masked histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
plt.plot(masked_hist)
plt.xlim(([0,256]))
plt.show()

#colored histogram
mask2 = cv.bitwise_and(img, img, mask = circle)
colors = ('b','g','r')
plt.figure()
plt.title('coloured histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)
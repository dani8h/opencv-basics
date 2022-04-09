import cv2 as cv

img = cv.imread('photos\\flower.jpg')
img = cv.resize(img,(int(img.shape[1]*0.9),int(img.shape[0]*0.6)),interpolation = cv.INTER_AREA)
cv.imshow('flower',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)



#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('simple threshold',thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('simple threshold inverse',thresh_inv)

#Adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5)
cv.imshow('adaptive thresholding', adaptive_thresh)


cv.waitKey(0)
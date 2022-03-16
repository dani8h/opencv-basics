import cv2 as cv
import numpy as np

img = cv.imread('photos\wp4789300-naruto-uzumaki-4k-wallpapers.jpg')
frame = cv.resize(img,(int(img.shape[1]*0.22),int(img.shape[0]*0.22)),interpolation = cv.INTER_AREA)
cv.imshow('naruto',frame)

#translation
def translate(frame, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(frame, transMat, dimensions)

translated = translate(frame, 300, 50)
cv.imshow('translated',translated)



#Rotation
def rotate(frame, angle, rotpoint=None):
    (height, width) = frame.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(frame,rotMat,dimensions)

rotated = rotate(frame, 45)
cv.imshow('rotated',rotated)


#Resizing

resized2 = cv.resize(frame,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized twice', resized2)


#Flipping
flip = cv.flip(frame,0)
cv.imshow('flipped',flip)

cv.waitKey(0)
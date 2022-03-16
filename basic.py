import cv2 as cv

img = cv.imread('photos\wp4789300-naruto-uzumaki-4k-wallpapers.jpg')
frame = cv.resize(img,(int(img.shape[1]*0.22),int(img.shape[0]*0.22)),interpolation = cv.INTER_AREA)
cv.imshow('naruto',frame)

# #converting to grayscale
# gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)


#blur
# blur = cv.GaussianBlur(frame,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)


# #create an edge cascade
# canny = cv.Canny(frame,125,175)
# a = cv.Canny(frame,0,0)
# cv.imshow('experiment',a)
# cv.imshow('Canny',canny)


# #dilate image
# dilated = cv.dilate(canny,(7,7), iterations=1)
# cv.imshow('dilated',dilated)

# #eroding - basically the opposite of canny

# eroded = cv.erode(dilated,(7,7),iterations=1)
# cv.imshow('eroded',eroded)

#cropping - this one is not correct
# cropy = frame[100:100, 200:200]
# cv.imshow('cropped',frame)


cv.waitKey(0)
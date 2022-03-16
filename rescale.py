import cv2 as cv


def rescaleFrame(frame,scale=0.22):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#rescaling image
img = cv.imread('photos\wp4789300-naruto-uzumaki-4k-wallpapers.jpg')
cv.imshow('naruto', img)
img_resized = rescaleFrame(img)
cv.imshow('resized',img_resized)
cv.waitKey(0)

# rescaling video
# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
#     cv.imshow('Video',frame)
#     cv.imshow('Resized',frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
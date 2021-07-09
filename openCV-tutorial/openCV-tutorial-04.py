import cv2 as cv
import numpy as np
import random

rotangle = 0

img = cv.imread('/Users/TeZ/Documents/PY/mypy/openCV-tutorial/cat.jpg')


# TRANSLATION
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, -100, 100)


# ROTATION
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)

# RESIZING
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)


# FLIPPING
flipped = cv.flip(img, -1)  # 0 = vertical  //  1 = horizontal // -1 = both
# cv.imshow('flipped', flipped)

# CROPPING
cropped = img[100:200, 300:400]
cv.imshow('cropped', cropped)

while True:
    # rotangle += 2
    # rotated = rotate(img, rotangle)
    # cv.imshow('rotated', rotated)

    k = cv.waitKey(33)
    if k == 27:    # Esc key to stop
        break

# cv.imshow('orig', img)
# cv.imshow('transated', translated)


cv.waitKey(0)

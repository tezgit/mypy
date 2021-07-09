import cv2 as cv
import numpy as np
import random


img = cv.imread('/Users/TeZ/Documents/PY/mypy/openCV-tutorial/cat.jpg')

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)

# canny edge detector / edge cascade
canny = cv.Canny(blur, 125, 175)

# dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)

# eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)

# resize
resized = cv.resize(gray, (200, 400))

# crop
cropped = img[50:200, 200:400]


cv.imshow('orig-img', img)
# cv.imshow('canny', canny)
# cv.imshow('dilated', dilated)
# cv.imshow('resized', resized)
cv.imshow('cropped', cropped)


cv.waitKey(0)

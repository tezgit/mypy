import cv2 as cv
import numpy as np
import TezOSC

img = cv.imread('/Users/TeZ/Documents/PY/mypy/openCV-tutorial/cat.jpg')
cv.imshow("original", img)

# make a blank image to draw contours later on
blank = np.zeros(img.shape, dtype="uint8")
# cv.imshow("Blank", blank)


# COUNTOUR DETECTION

# grayscale conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# canny edge detection
canny = cv.Canny(blur, 195, 225)  # threshold values 125, 175
cv.imshow("Canny", canny)


# threshold "binarizes" the image >> if pixel < fisrt  vlaue then black, if pixel > first value then (second value)
ret, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
# cv.imshow("Thresh", thresh)


# find contours (pass edges image)
# countours is a list of all the coordinates of all the corners found in the image
# hierarchies is the hierarchical representation of the shapes found in the  image
# RETR_LIST returns ALL the contours, EXTERNAL returns only the outer ones
# APPROX method NONE / SIMPLE (simple compresses the points and approx the vertices of a line)
contours, hierarchies = cv.findContours(
    canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)


# print(len(contours), 'contours found!')
print("%d contours found!" % (len(contours)))

cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow("CONTY", blank)

cv.waitKey(0)

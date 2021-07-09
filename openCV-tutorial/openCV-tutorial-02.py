import cv2 as cv
import numpy as np
import random
# import math


# giving it a shape of heightwidth/colordepth
rgb = np.zeros((500, 500, 4), dtype='uint8')

# format is BGR
rgb[:] = 50, 50, 50, 50

blank = cv.cvtColor(rgb, cv.COLOR_RGB2RGBA)

# cv.imshow('blank-image', blank)

cv.rectangle(blank, (0, 0),
             (blank.shape[1] // 2, blank.shape[0] // 2), (200, 200, 0), thickness=-1)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
          43, (0, 200, 0), thickness=3)

cv.line(blank, (0, 0),
        (blank.shape[1] // 1, blank.shape[0] // 1), (200, 200, 200, 10), thickness=5)

cv.putText(blank, "ciao", (blank.shape[0]//2,  blank.shape[1]//2),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 200), 2)

cv.imshow('blank-image', blank)

cv.waitKey(0)

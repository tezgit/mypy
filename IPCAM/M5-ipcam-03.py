import cv2 as cv
import numpy as np
from urllib.request import urlopen
import os
import datetime
import time
import sys
import argparse
import imutils
# import screeninfo


# get the size of the screen
screen_id = 1
is_color = False
# screen = screeninfo.get_monitors()[screen_id]
# width, height = screen.width, screen.height


# change to your ESP32-CAM ip
url = "http://192.168.0.220/cam.mjpeg"
# url = "http://192.168.0.234/cam.mjpeg"
CAMERA_BUFFER_SIZE = 4096
stream = urlopen(url)
bts = b''
i = 0

ww = 800
hh = 600
radius = int(hh / 2)

window_name = 'videostream'
cv.namedWindow(window_name, cv.WND_PROP_FULLSCREEN)
# cv.moveWindow(window_name, screen.x - 1, screen.y - 1)
cv.setWindowProperty(window_name, cv.WND_PROP_FULLSCREEN,
                     cv.WINDOW_FULLSCREEN)


while True:
    try:
        bts += stream.read(CAMERA_BUFFER_SIZE)
        jpghead = bts.find(b'\xff\xd8')
        jpgend = bts.find(b'\xff\xd9')
        if jpghead > -1 and jpgend > -1:
            jpg = bts[jpghead:jpgend+2]
            bts = bts[jpgend+2:]
            img = cv.imdecode(np.frombuffer(
                jpg, dtype=np.uint8), cv.IMREAD_UNCHANGED)
            # img=cv.flip(img,0) #>0:垂直翻轉, 0:水平翻轉, <0:垂直水平翻轉
            # h,w=img.shape[:2]
            #print('影像大小 高:' + str(h) + '寬：' + str(w))
            # img = cv.resize(img, (640, 480))

            img = cv.resize(img, (ww, hh))
            rotated = imutils.rotate(img, 180)

            mask = np.zeros(rotated.shape[:2], dtype="uint8")
            cv.circle(mask, (int(ww/2), int(hh/2)), radius, 255, -1)
            masked = cv.bitwise_and(rotated, rotated, mask=mask)

            cv.imshow(window_name, masked)
            # cv.imshow("a", rotated)

        k = cv.waitKey(1)
    except Exception as e:
        print("Error:" + str(e))
        bts = b''
        stream = urlopen(url)
        continue

    k = cv.waitKey(1)
    # 按a拍照存檔
    if k & 0xFF == ord('a'):
        cv.imwrite(str(i) + ".jpg", img)
        i = i+1
    # 按q離開
    if k & 0xFF == ord('q'):
        break
cv.destroyAllWindows()

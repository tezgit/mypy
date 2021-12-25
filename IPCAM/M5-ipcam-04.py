import cv2 as cv
import numpy as np
from urllib.request import urlopen
import os
import datetime
import time
import sys
import argparse
import imutils
from PIL import Image, ImageTk
from gi.repository import Gtk
import gi
gi.require_version("Gtk", "3.0")
window = Gtk.Window()
screen = window.get_screen()
ww = screen.get_width()
hh = screen.get_height()
print("screen width = {} ::: height = {}" .format(ww, hh))


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

radius = int(hh / 2)

window_name = 'videostream'
cv.namedWindow(window_name, cv.WND_PROP_FULLSCREEN)
# cv.moveWindow(window_name, screen.x - 1, screen.y - 1)
# cv.moveWindow(window_name, -1000, -1000)
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

            # rotated = imutils.rotate(img, 180)
            rotated = cv.flip(img, 0)
            resized = cv.resize(rotated, (1440, 900))

            #  cv2image = cv.cvtColor(img, cv.COLOR_BGR2RGBA)

            pilimg = Image.fromarray(img)
            # pilresized = pilimg.resize(ww, hh)

            # # resimg = cv.resize(img, (ww, hh))
            # rotated = imutils.rotate(resimg, 180)

            # opencvImage = cv.cvtColor(
            #     np.array(pilresized), cv.COLOR_RGB2BGR)

            # Convert RGB to BGR
            # open_cv_image = open_cv_image[:, :, ::-1].copy()

            tx, ty = ww / 4, hh / 4
            translation_matrix = np.array([
                [1, 0, tx], [0, 1, ty]], dtype=np.float32)
            translated_image = cv.warpAffine(
                src=resized, M=translation_matrix, dsize=(ww, hh))

            cv.imshow(window_name, translated_image)

            # mask = np.zeros(rotated.shape[:2], dtype="uint8")
            # cv.circle(mask, (int(ww/2), int(hh/2)), radius, 255, -1)
            # masked = cv.bitwise_and(rotated, rotated, mask=mask)
            # masked = cv.resize(masked, (ww, hh))

            # cv.imshow(window_name, masked)

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
    if k == 27:    # Esc key to stop
        break

cv.destroyAllWindows()


# ----------------------
# Upkey : 2490368
# DownKey : 2621440
# LeftKey : 2424832
# RightKey: 2555904
# Space : 32
# Delete : 3014656
# Esc: 27
# ----------------------

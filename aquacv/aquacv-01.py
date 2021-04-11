
# OpenCV Aquatic Explorer - TeZ - April 2021
# ==========================================
# refs:
# https://subscription.packtpub.com/book/application_development/9781788474443/1/ch01lvl1sec24/jumping-between-frames-in-video-files

import numpy as np
import cv2
import os
import pathlib
import sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

mypath = pathlib.Path(__file__).parent.absolute()
print('mypath: ' + str(mypath))
fd = os.open(str(mypath), os.O_RDONLY)
os.fchdir(fd)  # Use os.fchdir() method to change the dir


# change the file name if needed
fileName = str(mypath) + '/aquatix.mp4'  # /Users/TeZ/Documents/PY/mypy/aquacv/

cap = cv2.VideoCapture(fileName)  # load the video

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('Frame count:', frame_count)

while(cap.isOpened()):                    # play the video by reading frame by frame
    ret, frame = cap.read()
    if ret == True:
        # do some image processing here

        # Changing the colour-space
        LUV = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
        # Find edges
        edges = cv2.Canny(LUV, 10, 100)  # edges = cv2.Canny(LUV, 10, 100)
        # Find Contours
        contours, hierarchy = cv2.findContours(
            edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # Find Number of contours
        #  print("Number of Contours is: " + str(len(contours)))
        # Draw yellow border around two contours
        for nn in range(len(contours)):
            cv2.drawContours(frame, contours, nn, (0, 230, 255), 6)
        # qcv2.drawContours(frame, contours, 2, (0, 230, 255), 6)

        curframe = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

        # cv2.putText(frame, "frame:" + str(curframe), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (200, 200, 200), 4)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(frame)
        draw = ImageDraw.Draw(pil_im)
        font = ImageFont.truetype("Courier_New.ttf", 16)
        draw.text((20, 20), "frame: " + str(curframe),
                  (255, 255, 255), font=font)

        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        cv2.imshow('Contours', cv2_im_processed)
        # Show the image with contours
        # cv2.imshow('Contours', frame)

        # cv2.imshow('frame', frame)              # show the video
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('x'):
            curframe = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            if curframe < (frame_count - int(frame_count / 100)):
                cap.set(cv2.CAP_PROP_POS_FRAMES,
                        curframe + int(frame_count / 100))

    else:
        break

cap.release()
cv2.destroyAllWindows()

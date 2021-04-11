
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

window_name = "OCV-ANALYZER"

mypath = pathlib.Path(__file__).parent.absolute()
print('mypath: ' + str(mypath))
fd = os.open(str(mypath), os.O_RDONLY)
os.fchdir(fd)  # Use os.fchdir() method to change the dir

cons = False
constext = ["---","---","---","---"]
curframe = 0
hh = 100
lineh = 18

def console(pilimage, over):
    global curframe
    global hh
    global lineh
    
    # overlay = Image.new('RGBA', pil_im.size, (0,0,200,200))
    # odraw = ImageDraw.Draw(over)  # Create a context for drawing things on it.
    # odraw.rectangle(((0, pilimage.height - hh), (pilimage.width, pilimage.height)), fill=(0,155,0,50))
  
  

    c_0 = len(constext[0])
    c_1 = len(constext[1])
    c_2 = len(constext[2])
    c_3 = len(constext[3])
    
    fontsize = 12
    font = ImageFont.truetype("Courier_New.ttf", fontsize)
    
    # draw.rectangle(((2, pilimage.height - hh + 2), (len("console") * fontsize, pilimage.height - hh + 2 + fontsize )), fill=(0,0,200,255))
    over.text((10, pilimage.height - hh + 2), "console", (0, 0, 0, 255), font=font)
 
    
    draw.rectangle(((0, pilimage.height - hh + lineh), (c_0*fontsize, pilimage.height - hh + lineh * 1 + fontsize )), fill=(255,255,255,100))
    over.text((10, pilimage.height - hh + lineh*1), constext[0],(255, 255, 255, 255), font=font)
    draw.rectangle(((0, pilimage.height - hh + lineh * 2), (c_1*fontsize, pilimage.height - hh + lineh * 2 + fontsize )), fill=(255,255,255,100))
    over.text((10, pilimage.height - hh + lineh*2), constext[1],(255, 255, 255), font=font)
    draw.rectangle(((0, pilimage.height - hh + lineh * 3), (c_2*fontsize, pilimage.height - hh + lineh * 3 + fontsize )), fill=(255,255,255,100))
    over.text((10, pilimage.height - hh + lineh*3), constext[2],(255, 255, 255), font=font)
    draw.rectangle(((0, pilimage.height - hh + lineh * 4), (c_3*fontsize, pilimage.height - hh + lineh * 4 + fontsize )), fill=(255,255,255,100))  
    over.text((10, pilimage.height - hh + lineh*4), constext[3],(255, 255, 255), font=font)
    
    # pilimage = Image.composite(pilimage,over,over)


# change the file name if needed
fileName = str(mypath) + '/aquatic.mp4'  # /Users/TeZ/Documents/PY/mypy/aquacv/

cap = cv2.VideoCapture(fileName)  # load the video

cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

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
        
        constext[1] = "countours: " + str(len(contours)) 
             
             #cv2.putText(frame, "frame:" + str(curframe), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (200, 200, 200), 4)

        # qcv2.drawContours(frame, contours, 2, (0, 230, 255), 6)

        curframe = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        constext[0] = "frame: " + str(curframe)
       
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # pil_im = Image.fromarray(frame)
        # draw = ImageDraw.Draw(pil_im)
        # font = ImageFont.truetype("Courier_New.ttf", 16)
        # draw.text((20, 20), "frame: " + str(curframe),
        #           (255, 255, 255), font=font)

        # cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        # cv2.imshow('Contours', cv2_im_processed)
        
       
        
        r,c = frame.shape[:2]
        r_ = np.linspace(0,r,r+1)
        c_ = np.linspace(0,c,c+1)
        x_m, y_m = np.meshgrid(c_, r_, sparse=False, indexing='ij')

        
        
        
        
        ddept = cv2.CV_64F
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        x = cv2.Sobel(gray, ddept, 1,0, ksize=3, scale=1)
        y = cv2.Sobel(gray, ddept, 0,1, ksize=3, scale=1)
        absx= cv2.convertScaleAbs(x)
        absy = cv2.convertScaleAbs(y)
        edge = cv2.addWeighted(absx, 0.5, absy, 0.5,0)
        
        #========= PIL IMAGE ==========
        # TINT_COLOR = (200, 0, 0)  # red
        pil_im = Image.fromarray(edge)
        pil_im = pil_im.convert('RGBA')
        draw = ImageDraw.Draw(pil_im)
        
        overlay = Image.new('RGBA', pil_im.size, (0,0,0,255))
        odraw = ImageDraw.Draw(overlay)  # Create a context for drawing things on it.

        #====== CONSOLE CHECK ========
        if cons: 
            odraw.rectangle(((0, pil_im.height - hh), (pil_im.width, pil_im.height)), fill=(0,100,0,70))
            console(pil_im, odraw)
            pil_im = Image.composite(pil_im,overlay,overlay)
            
        
        #====== SHOW CV composite image ========
        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        cv2.imshow(window_name, cv2_im_processed)
     
       
        #======  KEYSTROKES  ===================
        k = cv2.waitKey(33)
        if k==27:    # Esc key to stop
            break
        elif k == 99:
            cons = not cons
        elif k == 83:
            curframe = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            if curframe < (frame_count - int(frame_count / 100)):
                cap.set(cv2.CAP_PROP_POS_FRAMES,
                        curframe + int(frame_count / 100))

        # Upkey : 82
        # DownKey : 84
        # LeftKey : 81
        # RightKey: 83
        # Space : 32
        # Delete : 255

    else:
        break

cap.release()
cv2.destroyAllWindows()



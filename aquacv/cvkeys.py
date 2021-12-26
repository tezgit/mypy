import cv2
import os
import pathlib

mypath = pathlib.Path(__file__).parent.absolute()
print('mypath: ' + str(mypath))
fd = os.open(str(mypath), os.O_RDONLY)
os.fchdir(fd)  # Use os.fchdir() method to change the dir

# filename = str(mypath) + "/export/" + fname + ".png"

img = cv2.imread(str(mypath) + "/timecar.png")  # load a dummy image
while(1):
    cv2.imshow('img', img)
    k = cv2.waitKey(33)
    if k == 27:    # Esc key to stop
        break
    elif k == -1:  # normally -1 returned,so don't print it
        continue
    else:
        print(k)  # else print its value

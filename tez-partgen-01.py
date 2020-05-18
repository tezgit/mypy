from randpix import randpix
import keyboard
import time
import random
import os
import sys
import pygame as pyg
from pygame import gfxdraw
from pygame.locals import *

pyg.init()


class tpix:
    def __init__(self, x, y, rr, gg, bb):
        self.tx = x
        self.ty = y
        gfxdraw.pixel(surf, x, y, (rr, gg, bb, 255))

    def tmove(mx, my):
        self.tx = mx
        self.ty = my
        print("moving to " + str(mx) + str(my))
        gfxdraw.pixel(surf, mx, my, (0, 0, 255, 255))


Tarray = []

width = 300  # image width in pixels
height = 300  # image height in pixels
black = (0, 0, 0)
num = 0

# PyGame Init
# screen = pyg.display.set_mode((width, height), pyg.FULLSCREEN)
screen = pyg.display.set_mode((width, height))
pyg.display.set_caption('TEZPARTGEN')
screen.fill(black)
pyg.mouse.set_visible(False)

clock = pyg.time.Clock()

size = (width, height)
surf = pyg.Surface(size)


fd = os.open("Documents/PY/mypy", os.O_RDONLY)
# Use os.fchdir() method to change the dir
os.fchdir(fd)


# /////////////////////////////////////////////


def check_events():
    ##### CHECK EVENTS / KEYBOARD KEY PRESSED #####
    for event in pyg.event.get():
        # https://www.pygame.org/docs/ref/key.html
        if (event.type == pyg.KEYDOWN):
            if(event.key == pyg.K_ESCAPE):
                print("eXit")
                quit()
            elif(event.key == pyg.K_s):
                print("sAve")
                pyg.image.save(screen, "grabcreen.png")
            elif (event.key == pyg.K_r):
                rr = not(rr)
                print("red = ", rr)
            elif (event.key == pyg.K_g):
                gg = not(gg)
                print("green = ", gg)
            elif (event.key == pyg.K_b):
                bb = not(bb)
                print("blue = ", bb)


# ////////////////////////////////////////////////
# infinite loop
while True:
    check_events()

    # surf.fill(black)
    # clock.tick(10)
    rx = random.randint(0, width)
    ry = random.randint(0, height)
    rr = random.randint(0, 255)
    gg = random.randint(0, 255)
    bb = random.randint(0, 255)

    TT = tpix(rx, ry, rr, gg, bb)
    Tarray.append(TT)  # tpix()
    # Tarray[num].move(rx, ry)
    num += 1
    # print(Tarray)
    screen.blit(surf, (0, 0))
    pyg.display.update()
    # time.sleep(1)

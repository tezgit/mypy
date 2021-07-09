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
        self.rr = rr
        self.gg = gg
        self.bb = bb
        gfxdraw.pixel(surf, x, y, (rr, gg, bb, 255))

    def tmove(self):
        # print("moving to " + str(mx) + str(my))
        gfxdraw.pixel(surf, self.tx + random.randint(0, 10), self.ty + random.randint(0, 10),
                      (self.rr, self.gg, self.bb, 255))


Tmaxelements = 50
Tarray = []

width = 300  # image width in pixels
height = 300  # image height in pixels
black = (0, 0, 0)
num = 0


# screen = pyg.display.set_mode((width, height), pyg.FULLSCREEN)
screen = pyg.display.set_mode((width, height), pyg.NOFRAME)
pyg.display.set_caption('TEZPARTGEN')
screen.fill(black)
pyg.mouse.set_visible(False)
clock = pyg.time.Clock()
size = (width, height)
surf = pyg.Surface(size)


fd = os.open("Documents/PY/mypy", os.O_RDONLY)
# Use os.fchdir() method to change the dir
os.fchdir(fd)


# ///// INIT ARRAY OF OBJECTS / PARTICLES
for nn in range(Tmaxelements):
    Tarray.append(tpix(1, 1, 0, 0, 0))


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
            elif (event.key == pyg.K_f):
                print("nada")


while True:
    check_events()
    # check_tframes()

    # surf.fill(black)
    # clock.tick(10)
    rx = random.randint(0, width)
    ry = random.randint(0, height)
    rr = random.randint(0, 255)
    gg = random.randint(0, 255)
    bb = random.randint(0, 255)

    # TT = tpix(rx, ry, rr, gg, bb)
    # Tarray.append(TT)  # tpix()
    # Tarray[num].move(rx, ry)
    if (num < Tmaxelements):
        Tarray[num] = tpix(rx, ry, rr, gg, bb)
        num += 1
    # else:
    #     num = 0
    #     surf.fill(black)

    for tt in range(Tmaxelements):
        Tarray[tt].tmove()

    # print(Tarray)
    screen.blit(surf, (0, 0))
    pyg.display.update()
    # time.sleep(1)
    print("tarray_size = ", len(Tarray))

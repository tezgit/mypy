import keyboard
import time
import random
import os
import sys
import pygame as pyg
from pygame import gfxdraw
from pygame.locals import *
import math

pyg.init()

random.seed(a=None, version=2)

Tmaxelements = 23
Tarray = []
width = 800  # image width in pixels
height = 800  # image height in pixels
black = (0, 0, 0)
white = (255, 255, 255)
num = 0


class tezgrafobj:
    def __init__(self, x, y, rr, gg, bb):
        self.idnum = num
        self.tx = x
        self.ty = y
        self.rr = rr
        self.gg = gg
        self.bb = bb
        self.alf = random.randint(2, 50)
        self.alfx = random.random() + 0.1
        self.incx = random.random()
        self.incy = random.random()
        self.sininc = 0.05

        rrx = random.randint(0, 1)
        rry = random.randint(0, 1)
        if (rrx):
            self.dirx = 1
        else:
            self.dirx = -1
        if (rry):
            self.diry = 1
        else:
            self.diry = -1

        alfy = random.randint(0, 1)
        if (alfy):
            self.alfadir = 1
        else:
            self.alfadir = -1

        # gfxdraw.pixel(surf, x, y, (rr, gg, bb, self.alf))

    def tmove(self):
        self.sininc += 0.15
        self.tx += self.incx * self.dirx + \
            math.sin(self.alf / random.randint(1, 10))
        self.ty += self.incy * self.diry + \
            math.cos(self.alf / random.randint(1, 10))

        if (self.alfadir):
            self.alf += self.alfx / 10.
        else:
            self.alf -= self.alfx / 10.

        if(self.alf >= 1 and self.alf <= 255):
            mycolor = (self.rr, self.gg, self.bb, int(self.alf / 2))
            mycolor = (200, 200, 200, 0.1)
            # gfxdraw.pixel(surf, int(self.tx), int(self.ty), mycolor)
            # pyg.draw.circle(surf, mycolor, (int(self.tx), int(self.ty)), 1, 0)
            # xcoord = (int(self.tx), int(self.ty))
            xcoord = (400, 400)
            ycoord = (self.tx, self.ty+self.sininc)
            pyg.draw.aaline(surf, mycolor, xcoord, ycoord, 0)
            # if (self.idnum > 0 and num <= (Tmaxelements - 1)):
            #     ycoord = (Tarray[num].tx, Tarray[num].ty)
            #     pyg.draw.aaline(surf, mycolor, xcoord, ycoord, 0)
            # pyg.draw.circle(surf, mycolor, (int(self.tx), int(self.ty)), 1, 0)


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
    inalfa = random.randint(10, 20)
    Tarray.append(tezgrafobj(int(width / 2), int(height / 2), 200, 200, 200))


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


for tt in range(Tmaxelements):
    rx = random.randint(0, width)
    ry = random.randint(0, height)
    rr = random.randint(0, 255)
    gg = random.randint(0, 255)
    bb = random.randint(0, 255)
    Tarray[num] = tezgrafobj(rx, ry, rr, gg, bb)

if (num < Tmaxelements):
    num += 1
elif (num >= (Tmaxelements - 1)):
    print("num: ", num)


while True:
    check_events()

    random.seed(a=None, version=2)
    rx = random.randint(0, width)
    ry = random.randint(0, height)
    rr = random.randint(0, 255)
    gg = random.randint(0, 255)
    bb = random.randint(0, 255)

    for tt in range(Tmaxelements):
        Tarray[tt].tmove()

    screen.blit(surf, (0, 0))
    pyg.display.update()
    # time.sleep(0.05)
    # print("tarray_size = ", len(Tarray))

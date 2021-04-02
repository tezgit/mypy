import keyboard
import time
import random
import os
import sys
import pygame as pyg
from pygame import gfxdraw
from pygame.locals import *
import math
from PIL import Image, ImageDraw

pyg.init()

random.seed(a=None, version=2)

Tmaxelements = 93  # random.randint(10, 200)
Tarray = []
width = 800  # image width in pixels
height = 800  # image height in pixels
black = (0, 0, 0)
white = (255, 255, 255)
num = 0

# screen = pyg.display.set_mode((width, height), pyg.FULLSCREEN)
screen = pyg.display.set_mode((width, height), pyg.NOFRAME)
pyg.display.set_caption('TEZPARTGEN')
# screen.fill(black)
pyg.mouse.set_visible(False)
clock = pyg.time.Clock()
size = (width, height)
surf = pyg.Surface(size)

surf.fill((0, 0, 0))


def initParticles():
    print("init particles!")
    # surf.fill((200, 200, 200))

    # ///// INIT ARRAY OF OBJECTS / PARTICLES
    for nn in range(Tmaxelements):
        # tezgrafobj params: x, y, r, g, b, idnum
        Tarray.append(tezgrafobj(int(width / 2),
                                 int(height / 2), 200, 200, 0, nn))

    cFactor = [1, 1, 1]
    cFactor[random.randint(0, 2)] = random.randint(1, 3)
    print("cFactor = " + str(cFactor))

    for tt in range(Tmaxelements):
        rx = random.randint(0, width)
        ry = random.randint(0, height)
        rr = (random.randint(1, 55)) * cFactor[0]  # % 255
        gg = (random.randint(1, 55)) * cFactor[1]  # % 255
        bb = (random.randint(1, 55)) * cFactor[2]  # % 255
        inum = tt
        Tarray[tt] = tezgrafobj(rx, ry, rr, gg, bb, inum)


class tezgrafobj:
    def __init__(self, x, y, rr, gg, bb, inum):
        self.idnum = inum
        self.tx = x
        self.ty = y
        self.rr = rr
        self.gg = gg
        self.bb = bb
        self.sininc = random.randint(0, 10) / 10.
        self.alf = random.randint(2, 250)
        self.alfx = (random.random() + self.sininc) % 100
        self.incx = random.random() * self.sininc
        self.incy = random.random() * self.alfx
        self.typo = random.randint(0, 3)

        self.dirx = random.randint(0, 1)
        self.diry = random.randint(0, 1)
        alfy = random.randint(0, 1)

        if (alfy):
            self.alfadir = 1
            self.alf = 1
        else:
            self.alfadir = -1
            self.alf = 255

        # gfxdraw.pixel(surf, x, y, (rr, gg, bb, self.alf))

    def tmove(self):

        if(random.randint(0, 1) == 0):
            self.sininc += random.randint(0, 10) / 10.  # 0.25
        else:
            self.sininc -= random.randint(0, 10) / 10.  # 0.25

        mr = random.randint(0, 10) / 50. + 0.1

        if(self.dirx):
            self.tx += self.incx
        else:
            self.tx -= self.incx

        if(self.diry):
            self.ty += self.incy
        else:
            self.ty -= self.incy

        ytr = random.randint(2, 20)
        if(self.typo == 0):
            yty = math.sin(self.alf) / ytr
        elif(self.typo == 1):
            yty = math.cos(self.alf) / ytr
        elif(self.typo == 2):
            yty = self.alf / (math.cos(mr) + self.sininc)
        else:
            yty = math.atan(self.alf + 1)

        # --- MAIN MOVE EQUATIONS ---
        if(self.tx < width and self.tx > 0):
            self.tx -= (-1) * (math.sin(self.alfx*self.sininc))
        else:
            self.tx = random.randint(0, width)

        if(self.ty < height and self.ty > 0):
            self.ty -= (-1) * (math.cos(self.alf*self.sininc))
        else:
            self.ty = random.randint(0, height)

        aar = random.randint(1, 50) / 50.
        if(self.alfadir):
            self.alf = int(self.alf + aar) % 255
        else:
            self.alf = int(self.alf - aar) % 255

        mycolor = (self.rr, self.gg, self.bb, self.alf)
        gfxdraw.pixel(surf, int(self.tx), int(self.ty), mycolor)

        xcoord = (400, 400)
        ycoord = (400, 400)


initParticles()

fd = os.open("/Users/TeZ/Documents/PY/mypy", os.O_RDONLY)
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
                pyg.image.save(screen, "grabcreen.jpg")
            elif (event.key == pyg.K_r):
                rr = not(rr)
                print("red = ", rr)
            elif (event.key == pyg.K_g):
                gg = not(gg)
                print("green = ", gg)
            elif (event.key == pyg.K_b):
                bb = not(bb)
                print("blue = ", bb)
            elif (event.key == pyg.K_i):
                initParticles()


def generate_gradient(
        colour1: str, colour2: str, width: int, height: int) -> Image:
    """Generate a vertical gradient."""
    base = Image.new('RGB', (width, height), colour1)
    top = Image.new('RGB', (width, height), colour2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        for x in range(width):
            mask_data.append(int(255 * (y / height)))
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base


grad = generate_gradient((0, 0, 0), (200, 200, 200), 800, 800)
# grad.show()

gr_mode = grad.mode
gr_size = grad.size
gr_data = grad.tobytes()

gr_image = pyg.image.fromstring(gr_data, gr_size, gr_mode)
screen.blit(gr_image, (0, 0))

# =============== MAIN LOOP  ==============================
while True:

    check_events()

    screen.blit(gr_image, (0, 0))
    # pyg.display.update()

    for tt in range(Tmaxelements):
        Tarray[tt].tmove()

    screen.blit(surf, (0, 0))

    pyg.display.update()
    # time.sleep(0.05)
    # print("tarray_size = ", len(Tarray))
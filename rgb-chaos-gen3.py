from randpix import randpix
import keyboard
import time
import random
import os
import sys
import pygame as pyg
from pygame import gfxdraw
from pygame.locals import*

pyg.init()

# Print current working directory
print("Current working dir : ",  os.getcwd())
# Now open a directory "/tmp"
fd = os.open("JUPY/", os.O_RDONLY)
# Use os.fchdir() method to change the dir
os.fchdir(fd)
# Print current working directory
print("Current working dir : ",  os.getcwd())


DEN = 5000  # density of pixels (for each color)
width = 1200  # image width in pixels
height = 300  # image height in pixels
alphamin = 250
alphamax = 250

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)
rr = True
gg = True
bb = True


# PyGame Init
screen = pyg.display.set_mode((width, height), pyg.FULLSCREEN)
pyg.display.set_caption('RGB-CHAOSGEN')
screen.fill(black)
pyg.mouse.set_visible(False)

clock = pyg.time.Clock()

size = (width, height)
surf = pyg.Surface(size)

# ////////////////////////////////////////////////


# ////////////////////////////////////////////////
def randpix():
    x = random.randint(1, width - 1)
    y = random.randint(1, height - 1)
    c = random.randint(0, 3)
    al = random.randint(50, 250)
    col = (255, 0, 0)
    alpha = random.randint(alphamin, alphamax)

    if (c == 0):
        if (rr):
            gfxdraw.pixel(surf, x, y, (255, 0, 0, alpha))
    elif (c == 1):
        if (gg):
            gfxdraw.pixel(surf, x, y, (0, 255, 0, alpha))
    elif (c == 2):
        if(bb):
            gfxdraw.pixel(surf, x, y, (0, 0, 255, alpha))
    return


# ////////////////////////////////////////////////
# infinite loop
while True:
    for event in pyg.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pyg.QUIT:

            # deactivates the pygame library
            pyg.quit()

            # quit the program.
            quit()

    for x in range(DEN):
        r = randpix()
        # Draws the surface object to the screen.
    screen.blit(surf, (0, 0))
    pyg.display.update()
    surf.fill(black)
    # clock.tick(10)

    ##### CHECK EVENTS / KEYBOARD KEY PRESSED #####
    for event in pyg.event.get():
        # https://www.pygame.org/docs/ref/key.html
        if (event.type == pyg.KEYDOWN):
            if(event.key == pyg.K_ESCAPE):
                print("eXit")
                quit()
            elif(event.key == pyg.K_s):
                print("sAve")
                pyg.image.save(screen, "rgbchaoscreen.jpg")
            elif (event.key == pyg.K_r):
                rr = not(rr)
                print("red = ", rr)
            elif (event.key == pyg.K_g):
                gg = not(gg)
                print("green = ", gg)
            elif (event.key == pyg.K_b):
                bb = not(bb)
                print("blue = ", bb)

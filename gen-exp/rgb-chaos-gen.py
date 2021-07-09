# from PIL import Image
# import IPython.display as display
import time
import random
import numpy as np
import os
import sys

import pygame as pyg
pyg.init()

DEN = 10000  # density of pixels (for each color)
width = 1200  # image width in pixels
height = 300  # image height in pixels
alpha = 255  # alpha level (same for all pixels)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

# PyGame Init
screen = pyg.display.set_mode((width, height))
pyg.display.set_caption('RGB-CHAOSGEN')
screen.fill(black)

clock = pyg.time.Clock()


# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
# img = Image.new('RGBA', (width, height), "black")  # create a new black image


def randpix():

    x = random.randint(1, width - 1)
    y = random.randint(1, height - 1)
    c = random.randint(0, 3)
    al = random.randint(50, 250)

    if (c == 0):
        pyg.draw.circle(screen, (255, 0, 0), (x, y), 1, 0)
    elif(c == 1):
        pyg.draw.circle(screen, (0, 255, 0), (x, y), 1, 0)
    elif(c == 2):
        pyg.draw.circle(screen, (0, 0, 255), (x, y), 1, 0)
    # pyg.display.update()
    return


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
    pyg.display.update()
    screen.fill(black)
    clock.tick(10)
# time.sleep(5)

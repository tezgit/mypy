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
import timer
from ftplib import FTP
import pathlib

physpath = pathlib.Path(__file__).parent.absolute()
print('physpath: ' + str(physpath))
fd = os.open(str(physpath), os.O_RDONLY)
os.fchdir(fd)  # Use os.fchdir() method to change the dir

ftp = FTP('ftp.phonomena.net')

gnum = 0


#  ===== ORIG STARTS HERE
pyg.init()

random.seed(a=None, version=2)

Tmaxelements = 93  # random.randint(10, 200)
Tarray = []
graVits = []
width = 800  # image width in pixels
height = 800  # image height in pixels
black = (0, 0, 0)
white = (255, 255, 255)
gnum = 0
cFactor = [1, 1, 1]


# screen = pyg.display.set_mode((width, height), pyg.FULLSCREEN)
screen = pyg.display.set_mode((width, height), pyg.NOFRAME)
pyg.display.set_caption('TEZPYGEN')
# screen.fill(black)
pyg.mouse.set_visible(False)
clock = pyg.time.Clock()
size = (width, height)
surf = pyg.Surface(size)
fname = "---"

pyg.font.init()
myfont = pyg.font.SysFont('Courier', 10)

# display_surface = pygame.display.set_mode((X, Y))

SAVETIME = 2 * 60 * 1000  # mm * ss *  ms
TEZTIME_EVENT = pyg.USEREVENT
pyg.time.set_timer(TEZTIME_EVENT, SAVETIME)

# /////////////////////////////////////////////


def ftpConnect(x_user, x_pwd):
    global ftp
    # ftp.login(user='phonomena.net', passwd='phonotez.23')
    ftp.login(user=x_user, passwd=x_pwd)
    welcomessage = ftp.getwelcome()
    print(">>> " + welcomessage)
    ftp.set_debuglevel(0)
    ftp.cwd('/')
    print("Current Directory >>> " + ftp.pwd())
    ftp.dir()

# /////////////////////////////////////////////


def grabFile(thisfile):
    filename = thisfile
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    localfile.close()

# /////////////////////////////////////////////


def placeFile(localfile, remotefile):
    # filename = thisfile  # 'testUpload.pdf'
    ftp.storbinary('STOR ' + remotefile, open(localfile, 'rb'))

# /////////////////////////////////////////////


def cfind(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

# /////////////////////////////////////////////


def makeDir(newdir):
    # The nlst()  method internally sends and NLST command to the
    # FTP server and returns the response as a list of names present
    # in the specified directory.

    for name in ftp.nlst():
        print(name)

    folderName = newdir
    if folderName in ftp.nlst():  # can also be ftp.nlst(yourfolder)
        print('hey hey folder ' + folderName + ' already exists')
    else:
        print("trying to make folder: " + folderName)
        ftp.mkd(folderName)
        print('naaissss!!  new folder ' + folderName + " created")
    ftp.cwd(folderName + "/")
    print("Your Remote Current Directory >>> " + ftp.pwd())


# /////////////////////////////////////////////


def initParticles():
    print("init particles!")
    # surf.fill((0, 0, 0))

    # --- INIT ARRAY OF OBJECTS / PARTICLES
    for nn in range(Tmaxelements):
        # tezgrafobj params: x, y, r, g, b, idnum
        Tarray.append(tezgrafobj(int(width / 2),
                                 int(height / 2), 200, 200, 0, nn))

    # --- INIT GRAVITY CENTERS
    numgravits = random.randint(2, 7)
    for gg in range(1, numgravits):
        g_x = random.randint(1, width)
        g_y = random.randint(1, height)
        g_tup = (g_x, g_y)
        graVits.append(g_tup)

    print("graVits: " + str(len(graVits)) + "  >>> " + str(graVits))

    # --- INIT COLOR BALANCE

    for cc in range(0, 3):
        cFactor[random.randint(0, cc)] = random.randint(0, 2)
    print("cFactor = " + str(cFactor))

    for tt in range(Tmaxelements):
        rx = random.randint(0, width)
        ry = random.randint(0, height)
        rr = (random.randint(1, 77)) * cFactor[0]  # % 255
        gg = (random.randint(1, 77)) * cFactor[1]  # % 255
        bb = (random.randint(1, 77)) * cFactor[2]  # % 255
        inum = tt
        Tarray[tt] = tezgrafobj(rx, ry, rr, gg, bb, inum)

# /////////////////////////////////////////////


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

    def recolor(self):
        if (random.randint(0, 1) == 0):
            blk = random.randint(0, 15)
            self.rr = blk
            self.gg = blk
            self.bb = blk
        else:
            self.rr = (random.randint(1, 77)) * cFactor[0]
            self.gg = (random.randint(1, 77)) * cFactor[1]
            self.bb = (random.randint(1, 77)) * cFactor[2]

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
        if (self.tx < width and self.tx > 0):
            # print("in-x")
            self.tx -= (-1) * (math.sin(self.alfx*self.sininc))
        else:
            Tarray[self.idnum].recolor()
            r_elem = random.randint(0, len(graVits)-1)
            x_elem = graVits[r_elem]
            self.tx = x_elem[0]  # random.randint(0, width)
            self.ty = x_elem[1]

        if(self.ty < height and self.ty > 0):
            self.ty -= (-1) * (math.cos(self.alf*self.sininc))
        else:
            Tarray[self.idnum].recolor()
            r_elem = random.randint(0, len(graVits)-1)
            y_elem = graVits[r_elem]
            self.ty = y_elem[1]  # random.randint(0, width)
            self.tx = y_elem[0]

        aar = random.randint(1, 50) / 50.
        if(self.alfadir):
            self.alf = int(self.alf + aar) % 255
        else:
            self.alf = int(self.alf - aar) % 255

        mycolor = (self.rr, self.gg, self.bb, self.alf)
        gfxdraw.pixel(surf, int(self.tx), int(self.ty), mycolor)

        xcoord = (400, 400)
        ycoord = (400, 400)

# /////////////////////////////////////////////


def genstart():
    ftpConnect('phonomena.net', 'phonotez.23')  # open FTP session
    # makeDir('physaria')

    localtime = time.localtime(time.time())
    pdate = str(localtime[0]) + str(localtime[1]) + str(localtime[2])
    datetime = str(localtime[0]) + str(localtime[1]) + str(localtime[2]) + \
        "_" + str(localtime[3]) + str(localtime[4]) + str(localtime[5])

    global gnum
    gnum += 1
    global graVits
    graVits = []
    surf.fill((200, 200, 200))

    global fname
    fname = "physaria-" + str(gnum) + "_" + datetime
    filename = str(physpath) + "/export/" + fname + ".png"
    # save to local disk

    if (gnum > 1):
        textsurface = myfont.render(fname, True, (0, 0, 0))
        screen.blit(textsurface, (width - (len(fname)*7), height - 20))
        pyg.display.update()

        pyg.image.save(screen, filename)
        print("file saved: " + filename)

    initParticles()
    print("gen restarted: " + str(gnum))

    # save to remote ftp server
    remotedir = pdate
    if (gnum == 1):
        ftp.cwd("/physaria")
        makeDir(remotedir)
        uploadcss()
        # ftp.cwd(remotedir)

    remotefilename = "/physaria/" + remotedir + "/" + fname + ".png"
    if (gnum > 1):
        # upload file to ftp server
        placeFile(filename, remotefilename)
        print("remotefilename: " + str(remotefilename) + " saved via FTP")

    rr = random.randint(40, 230)
    SAVETIME = 1 * rr * 1000
    pyg.time.set_timer(TEZTIME_EVENT, SAVETIME)


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
        elif (event.type == TEZTIME_EVENT):
            genstart()


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

# /////////////////////////////////////////////


def uploadcss():
    # makeDir("css")
    # ftp.cwd("css")
    placeFile("css/caption-gallery.css", "caption-gallery.css")
    placeFile("css/gallery.css", "gallery.css")
    placeFile("css/gallery.js", "gallery.js")
    placeFile("css/index.php", "index.php")
    placeFile("css/nocaption-index.php", "nocaption-index.php")


# ===== INIT HERE ======
ftpConnect('phonomena.net', 'phonotez.23')  # open FTP session
makeDir('physaria')


grad = generate_gradient((0, 0, 0), (200, 200, 200), 800, 800)
# grad.show()

gr_mode = grad.mode
gr_size = grad.size
gr_data = grad.tobytes()

gr_image = pyg.image.fromstring(gr_data, gr_size, gr_mode)
screen.blit(gr_image, (0, 0))


genstart()

# =============== MAIN LOOP  ==============================
while True:

    check_events()

    for tt in range(Tmaxelements):
        Tarray[tt].tmove()

    screen.blit(surf, (0, 0))

    pyg.draw.rect(surf, (200, 200, 200),
                  (width-(len(fname)*7)-5, height-20, len(fname)*6.4, 14))
    # textsurface = myfont.render(fname, True, (0, 0, 0))
    # screen.blit(textsurface, (width - (len(fname)*7), height - 20))

    pyg.display.update()

ftp.quit()  # close FTP session

import pygame as pyg
import random
import time
import funkz as f

print("pygame ver: " + pyg.version.ver)
pyg.init()  # init pygame video system

width = 400  # image width in pixels
height = 400  # image height in pixels
black = (0, 0, 0)
white = (255, 255, 255)
msgflag = False
mystring = "---"
msgfont = pyg.font.SysFont(None, 24)

# screen = pyg.display.set_mode((width, height), pyg.NOFRAME)
screen = pyg.display.set_mode((width, height))
pyg.display.set_caption('TNG-INST-APP')
print(pyg.display.Info())


def blink():
    global msgflag
    global mystring

    if(msgflag == False):

        ll = len(f.messages)
        if(ll > 0):
            mystring = str(f.messages[ll-1])
            f.messages.pop()
        msgflag == True
        msgbar(0)
        #  = font.render(mystring, True,  (0, 0, 190))


def filebar():
    pyg.draw.rect(screen, pyg.Color(100, 100, 100),
                  pyg.Rect(4, height-84, width-6, 30), 2)
    pyg.display.flip()
    pyg.display.update()


def msgbar(mode):
    global msgfont
    global mystring

    if(mode == 0):
        pyg.draw.rect(screen, pyg.Color(0, 20, 20),
                      pyg.Rect(2, height-32, width-4, 30), 0)

    else:
        msgflag == True
        pyg.draw.rect(screen, pyg.Color(150, 0, 0),
                      pyg.Rect(2, height-32, width-4, 30), 0)
    pyg.display.flip()
    # msgfont = pyg.font.SysFont(None, 20)
    img = msgfont.render(mystring, True,  (170, 170, 170))
    screen.blit(img, (20, height - 24))
    pyg.display.update()


def check_events():
    ##### CHECK EVENTS / KEYBOARD KEY PRESSED #####
    for event in pyg.event.get():
        # https://www.pygame.org/docs/ref/key.html
        if (event.type == pyg.KEYDOWN):
            if(event.key == pyg.K_ESCAPE):
                # clear terminal console
                # f.os.system('cls' if f.os.name == 'nt' else 'clear')
                print("eXit")
                quit()

        if (event.type == BLINKTIME_EVENT):
            blink()


msgbar(0)  # draw message bar
filebar()  # draw file box

BLINKTIME = 1000
BLINKTIME_EVENT = pyg.USEREVENT + 1
pyg.time.set_timer(BLINKTIME_EVENT, BLINKTIME)

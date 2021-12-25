import sys
import time
import pygame as pyg
import funkz as f


width = 400  # image width in pixels
height = 400  # image height in pixels
black = (0, 0, 0)
white = (255, 255, 255)


pyg.init()  # init video system
screen = pyg.display.set_mode((width, height), pyg.NOFRAME)
pyg.display.set_caption('TNG-INST-APP')


vPlayers = ["VP1", "VP2", "VP3"]
totplayers = len(vPlayers)
currSeq = 1

print("totplayers: " + str(totplayers) + " " + vPlayers[0])

f.nextFileName(2, currSeq)


def test_clients():
    # f.client1.publish(
    #     "sa1/url", "http://www.phonomena.net/test/v_1_01.mp4")  # publish
    # f.client1.publish("sa1/command", "noloop")
    # f.client1.publish("sa1/command", "mute")
    # f.client1.publish(
    #     "sa2/url", "http://www.phonomena.net/test/v_2_01.mp4")  # publish
    f.client1.publish(
        "sa1/url", "http://www.phonomena.net/test/v_1_01.mp4")  # publish
    f.client1.subscribe("events/ended", 1)
    f.client1.loop_start()


test_clients()  # test videos on players


# /////////////////////////////////////////////
def check_events():
    ##### CHECK EVENTS / KEYBOARD KEY PRESSED #####
    for event in pyg.event.get():
        # https://www.pygame.org/docs/ref/key.html
        if (event.type == pyg.KEYDOWN):
            if(event.key == pyg.K_ESCAPE):
                print("eXit")
                quit()


while True:
    check_events()

quit()

# while len(f.messages) > 0:
#     print(f.messages.pop(0))
# while not f.q.empty():
#     f.message = f.q.get()
#     print("queue: ", f.message)
# f.client1.disconnect()
# f.client1.loop_stop()

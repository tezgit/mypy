import sys
import time
import pyg
import funkz as f
import os
import logging


os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal console
logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')


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
        "sa1/url", "http://www.phonomena.net/test/v_2_01.mp4")  # publish


# /////////////////////////////////////////////


test_clients()  # test videos on players


while True:
    pyg.check_events()

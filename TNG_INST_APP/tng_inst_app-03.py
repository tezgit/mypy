import sys
import time
import pyg
import funkz as f
import os
import logging


os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal console
logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')


def test_clients():
    # f.client1.publish(
    #     "sa1/url", "http://www.phonomena.net/test/v_1_01.mp4")  # publish
    # f.client1.publish("sa1/command", "noloop")
    # f.client1.publish("sa1/command", "mute")
    # f.client1.publish(
    #     "sa2/url", "http://www.phonomena.net/test/v_2_01.mp4")  # publish
    nextfile = f.nextFileName(1, 1)
    f.client1.publish("VP1/url", nextfile)  # publish


# /////////////////////////////////////////////

# test_clients()  # test videos on players

f.v_play_next()

while True:
    pyg.check_events()

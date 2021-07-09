#########################################
# OSC INIT section
import argparse
import random
import time
import math
import time
import threading
import pygame as pyg
# from pythonosc import osc_message_builder
# from pythonosc import udp_client

from pythonosc.udp_client import SimpleUDPClient
from pythonosc import dispatcher
from pythonosc import osc_server

TRANSPA = 100  # use TezOSC.TRANSPA as variable name in other python files

print("sending 2 xOSC test messages")

oscdestIP = "127.0.0.1"  # "192.168.0.170"
port = 54321
client = SimpleUDPClient(oscdestIP, port)  # Create client
# test send
client.send_message("/test/floatparam", 123)   # Send float message
# Send message with int, float and string
client.send_message("/test/moreparams", [1, 2., "hello"])
#########################################


def transpa_handler(unused_addr, args, transp):
    global TRANSPA
    TRANSPA = transp


#########################################
if __name__ == "__main__":
    print("entered main OSC")
else:
    pass
    print("entered OSC module")
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=12345, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/filter", print)
    dispatcher.map("/transpa", transpa_handler, "console transparency")

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True  # true daemon exits when main program quits
    t.start()
    print("Serving on {}".format(server.server_address))
    # server.serve_forever()

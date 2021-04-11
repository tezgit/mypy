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

STROBE_RR = 0
STROBE_GG = 0
STROBE_BB = 200

STROBE_XR = 200
STROBE_XG = 0
STROBE_XB = 0

STROBO_MODE = 0


print("sending 2 xOSC test messages")

oscdestIP = "127.0.0.1"  # "192.168.0.170"
port = 54321
client = SimpleUDPClient(oscdestIP, port)  # Create client
# test send
client.send_message("/test/floatparam", 123)   # Send float message
# Send message with int, float and string
client.send_message("/test/moreparams", [1, 2., "hello"])
#########################################


def strobomode_handler(unused_addr, args, modo):
    # print("[{0}] ~ {1}".format(args[0], pippi))
    global STROBO_MODE
    STROBO_MODE = modo


def strobospeed_handler(unused_addr, args, freq):
    strobefreq = freq
    pyg.time.set_timer(pyg.USEREVENT + 2, strobefreq)
    # print("strobefreq = " + str(strobefreq))


def strobocolor_handler(unused_addr, args, scol):
    colorz = [i for i in map(int, scol.split(','))]
    # print("args >> " + str(args))
    global STROBE_RR
    global STROBE_GG
    global STROBE_BB
    STROBE_RR = colorz[0]
    STROBE_GG = colorz[1]
    STROBE_BB = colorz[2]


def stroboxcolor_handler(unused_addr, args, scol):
    colorz = [i for i in map(int, scol.split(','))]
    # print("xcol >> " + scol)
    global STROBE_XR
    global STROBE_XG
    global STROBE_XB
    STROBE_XR = colorz[0]
    STROBE_XG = colorz[1]
    STROBE_XB = colorz[2]


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
    dispatcher.map("/strobospeed", strobospeed_handler, "Strobo Speed")
    dispatcher.map("/strobocolor", strobocolor_handler, "Strobo Color")
    dispatcher.map("/stroboxcolor", stroboxcolor_handler, "Strobo X Color")
    dispatcher.map("/strobomode", strobomode_handler, "Strobo Mode")

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True  # true daemon exits when main program quits
    t.start()
    print("Serving on {}".format(server.server_address))
    # server.serve_forever()

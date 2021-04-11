import pygame as pyg

SAVETIME = 1 * 10 * 1000  # mm * ss *  ms
TEZTIME_EVENT = pyg.USEREVENT + 1
pyg.time.set_timer(TEZTIME_EVENT, SAVETIME)


strobefreq = 500
STROBETIME = 1 * 1 * strobefreq  # mm * ss *  ms
STROBETIME_EVENT = pyg.USEREVENT + 2
pyg.time.set_timer(STROBETIME_EVENT, STROBETIME)

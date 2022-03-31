#Filename: glow.py
#Description: Used to light the sensehat LEDs

import threading
import time
from sense_hat import SenseHat

sense = SenseHat()

_ = [  0,   0,   0] # off
r = [255, 140, 0] # yellow

GLOW = [
    _,_,r,r,r,r,_,_,
    _,r,r,r,r,r,r,_,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    _,r,r,r,r,r,r,_,
    _,_,r,r,r,r,_,_,
]

def setHeart(brightness):   
    r = [brightness, 0, 0]
    GLOW = [
        _,_,r,r,r,r,_,_,
        _,r,r,r,r,r,r,_,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        _,r,r,r,r,r,r,_,
        _,_,r,r,r,r,_,_,
    ]

def HeartBeat():
    sense.set_pixels(GLOW)

def HeartBeatThread():
    th = threading.Thread(target = HeartBeat)
    th.start()


def ClearHearBeat():
    sense.clear()

#ClearHearBeat()
#HeartBeatThread()


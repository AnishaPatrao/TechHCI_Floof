#Filename: glow.py
#Description: Used to light the sensehat LEDs

import threading
import time
from sense_hat import SenseHat

sense = SenseHat()

_ = [  0,   0,   0] # off
#r = [255, 0, 0] # red
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
    while(True):
        for i in range(0, 1):
            setHeart(i)
            sense.set_pixels(GLOW)
            time.sleep(0.005)
        
        for i in range(1, 0, -1):
            setHeart(i)
            sense.set_pixels(GLOW)
            time.sleep(0.005)
        
def HeartBeatThread():
    th = threading.Thread(target = HeartBeat)
    th.start()

HeartBeatThread()

def ClearHearBeat():
    sense.clear()

#ClearHearBeat()


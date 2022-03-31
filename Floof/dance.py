#Filename: dance.py
#Description: Used to light the connect with micro:bit

# import required modules
import os 
import time
from datetime import datetime 
from serial import Serial 

nextCompassPoll = 0.0 

#serial connectoion to the microbit - microbits device id is stored in the below path
serialDevDir='/dev/serial/by-id' 

#function to trigger the microbit
def StartDance():
    try:
        if (os.path.isdir(serialDevDir)):
            serialDevices = os.listdir(serialDevDir) 
            #print(serialDevices)
            if (len(serialDevices) > 0):
                serialDevicePath = os.path.join(serialDevDir, serialDevices[0])
                serial = Serial(port=serialDevicePath, baudrate=1200, timeout=0.2) 
                #send a serial signal to the microbit
                serial.write(b'1')
                time.sleep(15)
    except OSError as exception:
        raise
            
#StartDance()
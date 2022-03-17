import os 
import time
from datetime import datetime 
from serial import Serial 

nextCompassPoll = 0.0 

serialDevDir='/dev/serial/by-id' 

def StartDance():
    if (os.path.isdir(serialDevDir) ):
        serialDevices = os.listdir(serialDevDir) 

        if ( len(serialDevices) > 0 ):
            serialDevicePath = os.path.join(serialDevDir, serialDevices[0])
            #print(serialDevicePath)
            
            serial = Serial(port=serialDevicePath, baudrate=1200, timeout=0.2) 
            while(True):
                #receivedMsg = serial.readline() 
                serial.write(b'1')

StartDance()
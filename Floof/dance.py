import os 
import time
from datetime import datetime 
from serial import Serial 

nextCompassPoll = 0.0 

serialDevDir='/dev/serial/by-id' 

def StartDance():
    print("dance.py started")
    if (os.path.isdir(serialDevDir) ):
        serialDevices = os.listdir(serialDevDir) 
        print(serialDevices)
        if ( len(serialDevices) > 0 ):
            serialDevicePath = os.path.join(serialDevDir, serialDevices[0])
            serial = Serial(port=serialDevicePath, baudrate=1200, timeout=0.2) 
            serial.write(b'1')
            time.sleep(15)
            


#StartDance()
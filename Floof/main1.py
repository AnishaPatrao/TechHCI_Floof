import glow
import audio
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
                print('1')
                serial.write(b'1')
                time.sleep(3)


#glow the toy
#glow.heartBeat()
StartDance()
#PlayAudio("play")
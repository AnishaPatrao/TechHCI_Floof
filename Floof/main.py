import glow
import audio
import dance
import time
import random


#read accelerometer

#glow the toy and say hello
print("glow")
glow.HeartBeatThread()

print("sleep")
time.sleep(10)


while(True):
    randomActivity = random.randint(0,3)

    if randomActivity == 0:
        #TODO: wait for accelerometer to be stationary
        #audio
        print("dance audio")
        audio.PlayAudioThread("dance")
        time.sleep(3)
        #servo for dance
        print("dance")
        dance.StartDance()

        time.sleep(10)

    elif randomActivity == 1:

        print("story audio")
        audio.PlayAudioThread("story")

    elif randomActivity == 2:
        print("fun fact audio2")
        audio.PlayAudioThread("story")

    elif randomActivity == 3:
        print("fun fact audio3")
        audio.PlayAudioThread("story")

  



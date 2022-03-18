import glow
import audio
import dance
import time



#read accelerometer

#glow the toy
print("glow")
glow.HeartBeatThread()

print("sleep")
time.sleep(10)

#audio
print("dance audio")
audio.PlayAudioThread("dance")

#servo for dance
print("dance")
dance.StartDance()


print("story audio")
audio.PlayAudioThread("story")


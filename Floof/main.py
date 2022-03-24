from sense_hat import SenseHat
import glow
import audio
import dance
import time
import random
#import movement
import eventlet
import socketio
import threading
from flask import Flask
from flask import jsonify

app = Flask(__name__)
completedActivity = []
counter = 0
glow.ClearHearBeat()
isStarted = False
isPlaying = False
isShutdown = False
sense = SenseHat()

def RecordMovement():

    #while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=abs(x)
    y=abs(y)
    z=abs(z)

    if x>1 or y>1 or z>1:
        print("x: {0}, y: {1}, z: {2}".format(x,y,z))
        return True
    else:
        #sense.clear()
        return False
        #print("false")

    time.sleep(0.05)

def RunToy():

    print("RunToy")
    
    global isPlaying
    counter = 0
    while True:
        time.sleep(0.05)
        counter = counter + 1
        print(str(counter))

        #if RecordMovement() == True:
        if counter > 1000:
            isStarted = True
            print("isShutdown 1: " + str(isShutdown))
            return
            
            if isStarted == True and isShutdown == False:
                PlayActivities(completedActivity)
                print("Play activities finished")


def PlayActivities(completedActivity):
    isStarted = False
    isPlaying = True
    time.sleep(5)
    print("counter" + str(counter))
    glow.HeartBeatThread()
    audio.PlayAudio("Conv_IMissedYou")
    print(completedActivity)
    completedActivity.clear()
    
    while len(completedActivity) < 4:
        #print("isShutdown 2: " + str(isShutdown))

        #print("isPlaying in while: " + str(isPlaying))
        randomActivity = random.randint(1,4)
        if randomActivity not in completedActivity:

            if randomActivity != 1:
                completedActivity.append(randomActivity)
            
            if randomActivity == 1:
                
                if not RecordMovement():
                    print("dance sequence. activity:" + str(randomActivity))
                    
                    audio.PlayAudio("Activity_LetsDance")
                    audio.PlayAudioThread("Activity_Dance")
                    time.sleep(3)
                    #servo for dance
                    dance.StartDance()

                    time.sleep(15)
                    completedActivity.append(randomActivity)

            elif randomActivity == 2:

                print("fun fact 2. activity:" + str(randomActivity))
                audio.PlayAudio("FunFact_Octopus")
                time.sleep(5)

            elif randomActivity == 3:
                print("fun fact 3. activity:" + str(randomActivity))
                audio.PlayAudio("FunFact_StrongestMuscle")
                time.sleep(5)

            elif randomActivity == 4:
                print("fun fact 4. activity:" + str(randomActivity))
                audio.PlayAudio("FunFact_FavColor")
                time.sleep(5)
    #print("isPlaying end of while: " + str(isPlaying))
    
    isPlaying = False


def ShutDown():
    audio.PlayAudio("Conv_PlayWithMe")  
    glow.ClearHearBeat()

#def ScreenOn():
@app.route('/api/floof-sad/<int:isScreenOn>', methods=['GET'])
def play_sad_floof(isScreenOn):
    if isScreenOn == 1:
        IsShutdown = True
        print("play_sad_floof shutdown")
        print("isPlaying: " + str(isPlaying))
        print("thread: " + str(th))
        if isPlaying == True:
            while isPlaying == False:
                print("waiting...")

        #if th.isAlive():
        #th.kill()
        ShutDown()
    return None

lock = threading.Lock()
th = threading.Thread(target = RunToy)
with lock:
    th.start()
print("starting thread: " + str(th))

# lock = threading.Lock()
# th = threading.Thread(target = movement.RecordMovement)
# with lock:
#     th.start()
    
# RunToy()

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='groupb.local')


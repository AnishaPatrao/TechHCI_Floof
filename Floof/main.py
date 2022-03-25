from sense_hat import SenseHat
import glow
import audio
import dance
import time
import random
import eventlet
import socketio
import threading
from flask import Flask
from flask import jsonify

app = Flask(__name__)
completedActivity = []
counter = 0
glow.ClearHearBeat()
isPlaying = False
isShutdown = False
sense = SenseHat()

def RecordMovement():

    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=abs(x)
    y=abs(y)
    z=abs(z)

    if x>1.1 or y>1.1 or z>1.1:
        print("x: {0}, y: {1}, z: {2}".format(x,y,z))
        return True
    else:
        return False

    time.sleep(0.05)

def RunToy():

    print("RunToy")
    
    global isPlaying
    global isShutdown
    counter = 0
    isPlayedAudio = False

    while True:
        time.sleep(0.05)

        if RecordMovement() == True:
            
            if isShutdown == False:
                PlayActivities(completedActivity)
                isPlayedAudio = False
                print("Play activities finished")

            elif isShutdown == True and isPlayedAudio == False:
                audio.PlayAudio("Conv_PlayWithMe")  
                sense.clear()
                isPlayedAudio = True

        if isShutdown == True and isPlayedAudio == False:
            audio.PlayAudio("Conv_PlayWithMe")  
            sense.clear()
            isPlayedAudio = True


def PlayActivities(completedActivity):
    global isPlaying
    global isShutdown
    isPlaying = True
    time.sleep(1)
    print("counter" + str(counter))
    glow.HeartBeat()
    audio.PlayAudio("Conv_IMissedYou")
    print(completedActivity)
    completedActivity.clear()
    
    while len(completedActivity) < 4:
        if isShutdown == True:
            break

        randomActivity = random.randint(1,4)
        if randomActivity not in completedActivity and isShutdown == False:

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

                    time.sleep(2)
                    completedActivity.append(randomActivity)

            elif randomActivity == 2:

                print("fun fact 2. activity:" + str(randomActivity))
                audio.PlayAudio("FunFact_Octopus")
                time.sleep(3)

            elif randomActivity == 3:
                print("fun fact 3. activity:" + str(randomActivity))
                audio.PlayAudio("FunFact_StrongestMuscle")
                time.sleep(3)

            elif randomActivity == 4:
                print("fun fact 4. activity:" + str(randomActivity))
                audio.PlayAudio("FunFact_FavColor")
                time.sleep(3)
    
    isPlaying = False

#API for determining if the Ipad is being used by the child
@app.route('/api/floof-sad/<int:isScreenOn>', methods=['GET'])
def play_sad_floof(isScreenOn):
    global isShutdown 
    print("isScreenOn:" + str(isScreenOn))

    if isScreenOn == 1:
        isShutdown = True
        print("play_sad_floof shutdown")
        print("isPlaying: " + str(isPlaying))
        print("isShutdown:" + str(isShutdown))
    else:
        isShutdown = False
        print("isPlaying: " + str(isPlaying))
        print("isShutdown:" + str(isShutdown))

    return jsonify({'value': 'success'})

#Create a thread to run the toy, so that the main thread can listen for api calls from the iPad
lock = threading.Lock()
th = threading.Thread(target = RunToy)
with lock:
    th.start()
print("starting thread: " + str(th))

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='groupb.local')


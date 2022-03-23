import glow
import audio
import dance
import time
import random
import movement
import eventlet
import socketio
import threading
from flask import Flask
from flask import jsonify

app = Flask(__name__)
completedActivity = []
glow.ClearHearBeat()

def RunToy():
    while True:
        if movement.IsMoving():
            glow.HeartBeatThread()
            audio.PlayAudio("Conv_IMissedYou")
            print(completedActivity)
            completedActivity.clear()
            PlayActivities(completedActivity)


def PlayActivities(completedActivity):
    while len(completedActivity) < 4:

        randomActivity = random.randint(1,4)
        if randomActivity not in completedActivity:

            if randomActivity != 1:
                completedActivity.append(randomActivity)
            
            if randomActivity == 1:
                
                if not movement.IsMoving():
                    print("dance sequence. activity:" + randomActivity)
                    
                    audio.PlayAudioThread("Activity_LetsDance")
                    audio.PlayAudioThread("Activity_Dance")
                    time.sleep(3)
                    #servo for dance
                    dance.StartDance()

                    time.sleep(10)
                    completedActivity.append(randomActivity)

            elif randomActivity == 2:

                print("fun fact 2. activity:" + randomActivity)
                audio.PlayAudio("FunFact_Octopus")
                time.sleep(5)

            elif randomActivity == 3:
                print("fun fact 3. activity:" + randomActivity)
                audio.PlayAudio("FunFact_StrongestMuscle")
                time.sleep(5)

            elif randomActivity == 4:
                print("fun fact 4. activity:" + randomActivity)
                audio.PlayAudio("FunFact_FavColor")
                time.sleep(5)


def ShutDown():
    audio.PlayAudio("Conv_PlayWithMe")  
    glow.ClearHearBeat()

#def ScreenOn():
@app.route('/api/floof-sad/<int:isScreenOn>', methods=['GET'])
def play_sad_floof(isScreenOn):
    if isScreenOn == 1:
        print("play_sad_floof shutdown")
        if th.isAlive():
            th.kill()
        ShutDown()
    return None

th = threading.Thread(target = RunToy)
th.start()
    
#RunToy()

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='groupb.local')


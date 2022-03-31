#Filename: main.py
#Description: The main thread which listens for API calls and creates a thread which executes the toys functionality

# import required modules
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
import RPi.GPIO as GPIO
    
#function to record accelerometer movement to detect if the toy is moving
def RecordMovement():
    try:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x=abs(x)
        y=abs(y)
        z=abs(z)

        #movement is detected if the x, y and z readings are > 1.1
        if x>1.1 or y>1.1 or z>1.1:
            print("x: {0}, y: {1}, z: {2}".format(x,y,z))
            return True
        else:
            return False
    except:
        Error("Error in Recording accelerometer readings.")
        return False 

#function to run the entire toy functionality
def RunToy():
    global isShutdown
    counter = 0
    isPlayedAudio = False

    #run an infinite while loop to cycle through interactions 
    while True:
        time.sleep(0.05)

        try:
            #if movement is recorded, it switches on interactions
            if RecordMovement() == True:
                
                #check if the iPad is not in use and allow interactions
                if isShutdown == False:
                    PlayActivities(completedActivity)
                    isPlayedAudio = False
                    print("Play activities finished")

            #check if the iPad is in use and disallow interactions
            if isShutdown == True and isPlayedAudio == False:
                audio.PlayAudio("Conv_PlayWithMe")  
                sense.clear()
                isPlayedAudio = True
        except: 
            Error("Error in running toy. Continuing to next run.")

#function to play the activities
def PlayActivities(completedActivity):

    #global variables to allow communication between the toy thread and the webapi main thread
    global isShutdown

    time.sleep(1)

    try:
        #start up - glow the toy and play an audio
        glow.HeartBeat()
        audio.PlayAudio("Conv_IMissedYou")

        completedActivity.clear()
        
        #loop through the activities
        while len(completedActivity) < 4:
            if isShutdown == True:
                break

            randomActivity = random.randint(1,4)

            #do not repeat activities
            if randomActivity not in completedActivity and isShutdown == False:

                if randomActivity != 1:
                    completedActivity.append(randomActivity)
                
                if randomActivity == 1:
                    
                    #dance sequence if floof is not moving
                    if not RecordMovement():
                        audio.PlayAudio("Activity_LetsDance")

                        #play the dance audio on a separate thread so that the current thread can continue to trigger the servo movements
                        audio.PlayAudioThread("Activity_Dance")
                        time.sleep(3)
                        
                        #trigger the servos for dance through the microbit
                        dance.StartDance()

                        time.sleep(2)
                        completedActivity.append(randomActivity)

                elif randomActivity == 2:

                    #fun fact activity
                    audio.PlayAudio("FunFact_Octopus")
                    time.sleep(3)

                elif randomActivity == 3:
                    
                    #fun fact activity
                    audio.PlayAudio("FunFact_StrongestMuscle")
                    time.sleep(3)

                elif randomActivity == 4:
                    
                    #interactive activity
                    audio.PlayAudio("FunFact_FavColor")
                    time.sleep(3)
        
    except: 
            Error("Error in Playing activities. Continuing to next run.")

def Error(error):
    print(error)

try:
    #initialize Flask for web api calls
    app = Flask(__name__)

    #variable initilaizations
    completedActivity = []
    counter = 0
    isShutdown = False

    #initialize the sense hat
    sense = SenseHat()

    #clear the glow on initial startup
    glow.ClearHearBeat()

    #API for determining if the Ipad is being used by the child
    @app.route('/api/ipad-usage/<int:isScreenOn>', methods=['GET'])
    def ToggleToyState(isScreenOn):
        global isShutdown 
        #print("isScreenOn:" + str(isScreenOn))

        if isScreenOn == 1:
            #if the childs screen is on
            isShutdown = True
        else:
            #if the childs screen is off
            isShutdown = False

        return jsonify({'value': 'success'})

    #Create a thread to run the toy, so that the main thread can listen for api calls from the iPad
    lock = threading.Lock()
    th = threading.Thread(target = RunToy)
    with lock:
        th.start()
    #print("starting thread: " + str(th))

    if __name__ == '__main__':
        app.run(debug=False, port=5000, host='groupb.local')

finally:
        GPIO.cleanup

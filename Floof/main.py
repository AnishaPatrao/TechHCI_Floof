import glow
import audio
import dance
import time
import random
import movement
import eventlet
import socketio
import threading


def RunToy():
    while True:
        if movement.IsMoving():
            print("glow")
            glow.HeartBeatThread()
            audio.PlayAudio("Floof_Audio_I missed you")

            while(True):
                randomActivity = random.randint(0,3)

                if randomActivity == 0:
                    #TODO: wait for accelerometer to be stationary
                    #audio
                    if not movement.IsMoving():
                        print("dance audio")
                        
                        audio.PlayAudioThread("Floof_Audio_123 lets dance")
                        time.sleep(3)
                        #servo for dance
                        print("dance")
                        dance.StartDance()

                        time.sleep(10)

                elif randomActivity == 1:

                    print("story audio")
                    audio.PlayAudio("Floof_Audio_Learn-octopus")
                    time.sleep(5)

                elif randomActivity == 2:
                    print("fun fact audio2")
                    audio.PlayAudio("Floof_Audio_Learn-strongest muscle")
                    time.sleep(5)

        else:
            glow.ClearHearBeat()

th = threading.Thread(target = RunToy)
th.start()

sio = socketio.Server()
app = socketio.WSGIApp(sio)
print("socket")
def get_device_id(environ):
    print(environ.get('HTTP_DEVICE_ID', None))
    return environ.get('HTTP_DEVICE_ID', None)

@sio.event
def connect(sid, environ):
    print("socket")
    device_id = get_device_id(environ) or sid
    sio.save_session(sid, {'device_id': device_id})
    print('{} is connected'.format(device_id))

@sio.event
def my_message(sid, data):
    session = sio.get_session(sid)
    print('Received data from {}: {}'.format(session['device_id'], data))

@sio.event
def screen_opened(sid, data):
    session = sio.get_session(sid)
    print('Screen opened {}'.format(session['device_id']))
    #main.ShutDown()


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app, log_output=False)


#read accelerometer

#glow the toy and say hello

  
def ShutDown():
    audio.PlayAudio("Floof_Audio_I missed you")  
    glow.ClearHearBeat()




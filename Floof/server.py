import eventlet
import socketio
#import main

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

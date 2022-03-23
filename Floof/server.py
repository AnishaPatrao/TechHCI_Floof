from flask import Flask
from flask import jsonify
import audio

app = Flask(__name__)
@app.route('/')
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }

@app.route('/api/floof-sad', methods=['POST'])
def create_reading():
    #req_json = request.get_json()
    print(request.get_json())
    if isScreenOn:
        audio.PlayAudio("Floof_Audio_I missed you")
    #return "True"
    return jsonify({'status': 'succeeded'})

@app.route('/api/floof-sad/<int:isScreenOn>', methods=['GET'])
def play_sad_floof(isScreenOn):
    if isScreenOn:
        audio.PlayAudio("Floof_Audio_I missed you")
    return "True"
    
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='groupb.local')


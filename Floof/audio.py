# import required modules
import threading
from pydub import AudioSegment
from pydub.playback import play

PATH = "/home/pi/TechHCI/TechHCI_Floof/Floof/Audio/"
MP3EXTN = ".mp3"

# for playing mp3 file
def PlayAudio(sound):
    print('audio played:' + sound)
    song = AudioSegment.from_mp3(PATH + sound + MP3EXTN)
    play(song)

def PlayAudioThread(sound):
    print('audio thread: ' + sound)
    th = threading.Thread(target = PlayAudio, args = (sound, ))
    th.start()
    return th

#PlayAudioThread("Floof_Audio_I missed you")
#PlayAudio("Conv_IMissedYou")
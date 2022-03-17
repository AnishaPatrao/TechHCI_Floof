# import required modules
from pydub import AudioSegment
from pydub.playback import play

PATH = "/home/pi/Floof/Audio/"
MP3EXTN = ".mp3"

# for playing mp3 file
def PlayAudio(sound):
    print(sound)
    song = AudioSegment.from_mp3(PATH + sound + MP3EXTN)
    play(song)

PlayAudio("play")
import os
from pygame import mixer

MUSIC_FILE = "opening.wav"

mixer.init()
mixer.music.load(os.getcwd() + "/" + MUSIC_FILE)
mixer.music.play()

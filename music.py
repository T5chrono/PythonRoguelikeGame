from pygame import mixer
import os

class Music():

    MUSIC_FILE = "/main_theme.wav"
    
    def play_music():
        mixer.init()
        mixer.music.load(os.getcwd() + Music.MUSIC_FILE)
        mixer.music.play()
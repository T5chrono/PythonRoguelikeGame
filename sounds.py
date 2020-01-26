from pygame import mixer
import os

class Music():

    # MUSIC_FILE = "/opening.wav"
    DIRECTORY = os.getcwd() +"/events_sounds/"
    MAIN_THEME = "main_theme.wav"
    
    def play_music():
        mixer.init()
        mixer.music.load(Music.DIRECTORY + Music.MAIN_THEME)
        mixer.music.play(loops = -1)
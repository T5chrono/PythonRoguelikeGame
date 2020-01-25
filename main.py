import os
import util
import game
import ui
from pygame import mixer



MUSIC_FILE = "main_theme.wav"


def main():
    board_created = False
    util.clear_screen()

    mixer.init()
    mixer.music.load(os.getcwd() + "/" + MUSIC_FILE)
    mixer.music.play()

    character_name = ui.get_character_name()

    while not board_created:
        try:
            engine = game.Game()
        except TypeError:
            print("Enter a number!")
        else:
            board_created = True

    engine.create_new_board()
    engine.create_character(character_name)
    engine.board.display_board()

    while engine.is_running:
        engine.handle_actions()
       
    ui.display_goodbye(engine.player_character.name)


if __name__ == '__main__':
    main()

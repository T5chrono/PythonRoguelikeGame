import util
import game
import ui
import sounds
import colors
import os


def main():
    util.clear_screen()
    ui.UI.display_by_line(ui.IMAGES_DIRECTORY + ui.OPENING_FILE)
    engine = game.Game()
    sounds.Music.play_music()

    board_created = False
    
    while not board_created:
        try:
            engine.create_new_board()
        except TypeError:
            engine.UI.display_error_info("expected number")
        else:
            board_created = True

    engine.is_running = True

    character_name = engine.player_character.ui.get_user_value(ui.UI.PROVIDE_NAME, "Keanu")
    engine.add_character_name(character_name)
    engine.initialize_player_class_and_race()

    util.key_pressed()
    engine.UI.display_help()

    while engine.is_running:
        engine.handle_action()
       
    engine.UI.display_goodbye()


if __name__ == '__main__':
    main()

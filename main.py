import util
import game
import ui
import sounds
import colors

# import music


def main():
    util.clear_screen()

    character_name = ui.get_user_value("\nPlease provide the name of your character! ", "Keanu")

    # music.Music.play_music()

    board_created = False
    while not board_created:
        try:
            engine = game.Game()
        except TypeError:
            print(f"{colors.ERROR}Enter a number!{colors.RESET}")
        else:
            board_created = True

    engine.is_running = True

    engine.create_new_board()
    engine.create_character(character_name)
    engine.initialize_player_class_and_race()
    util.key_pressed()
    util.clear_screen()
    engine.board.display_board()
    engine.get_help(**engine.SUPPORTED_KEYS)

    while engine.is_running:
        engine.handle_action()
       
    ui.display_goodbye(engine.player_character.name)


if __name__ == '__main__':
    main()

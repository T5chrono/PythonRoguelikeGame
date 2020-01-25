import util
import game
import ui
import music


def main():
    util.clear_screen()

    music.Music.play_music()
    
    character_name = ui.get_character_name()

    board_created = False
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
        engine.handle_action()
       
    ui.display_goodbye(engine.player_character.name)


if __name__ == '__main__':
    main()

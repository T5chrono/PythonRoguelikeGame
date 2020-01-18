import util
import engine
import ui
import game


def main():
    is_running = True
    board_created = False

    while not board_created:
        try:
            engine = game.Game()
            board_created = True
        except TypeError:
            print("Enter a number!")

    engine.board.display_board()

    while is_running:
        player_move = util.key_pressed()
        if player_move in ["w", "s", "a", "d"]:
            try:
                engine.board.move_player(player_move)
                util.clear_screen()
                engine.board.display_board()
            except:
                util.clear_screen()
                engine.board.display_board()
                print("You can't move on wall!")


if __name__ == '__main__':
    main()

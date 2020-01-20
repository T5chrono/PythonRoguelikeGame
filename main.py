import util
import engine
import ui
import game
import board
import inventory
import character


def main():
    board_created = False

    while not board_created:
        try:
            engine = game.Game()
            board_created = True
        except TypeError:
            print("Enter a number!")

    engine.board.display_board()

    while engine.is_running:
        player_move = util.key_pressed()
        if player_move in ["w", "s", "a", "d"]:
            engine.handle_movement_effects(player_move)
        elif player_move == "c":
            print(character.Keanu)
        elif player_move == "h":
            pass # prints help menu
        elif player_move == "i":
            inventory.print_table(character.Keanu.inventory)
        elif player_move == "p":
            inventory.add_to_inventory(character.Keanu.inventory, ["some item to implement"])
        elif player_move == "q":
            engine.is_running = False


if __name__ == '__main__':
    main()

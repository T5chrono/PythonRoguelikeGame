import util
import engine
import ui
import game
import board
from inventory import print_table, add_to_inventory, random_item, ITEMS
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
            print(engine.player_character)
        elif player_move == "h":
            pass # prints help menu
        elif player_move == "i":
            print_table(engine.player_character.inventory)
        elif player_move == "p":
            if engine.board.tiles[engine.board.player_tile_position[0]][engine.board.player_tile_position[1]].tile_type == "ITEM":
                add_to_inventory(engine.player_character.inventory, random_item(ITEMS))
                engine.board.tiles[engine.board.player_tile_position[0]][engine.board.player_tile_position[1]].tile_type = "EMPTY"
            else:
                print("There is nothing here.")
        elif player_move == "q":
            engine.is_running = False


if __name__ == '__main__':
    main()
#engine.board.player_tile_position[0]
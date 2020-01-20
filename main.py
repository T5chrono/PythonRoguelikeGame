import util
import game
import weapons_armor_items
from inventory import print_table, add_to_inventory, random_item, ITEMS


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
            display_help()
        elif player_move == "i":
            print_table(engine.player_character.inventory)
        elif player_move == "p":
            pick_up_something(engine)
        elif player_move == "e":
            # TODO complete equiping logic:
            user_input = input("What would you like to equip?: ")
            if user_input in weapons_armor_items.weapon_names:# and user_input in engine.player_character.inventory.keys():
                for i in range(len(weapons_armor_items.weapon_names)):
                    if user_input == weapons_armor_items.weapon_names[i]:
                        add_to_inventory(engine.player_character.inventory, [engine.player_character.weapon.name])
                        engine.player_character.weapon = weapons_armor_items.weapons[i]
            elif user_input in weapons_armor_items.armor_names:
                pass
            else:
                print(f"You cannot equip {user_input}.")
        elif player_move == "q":
            engine.is_running = False


# Extracted methods from loop engine.is_running
def pick_up_something(engine):
    if engine.board.tiles[engine.board.player_tile_position[0]][
                          engine.board.player_tile_position[1]].tile_type == "ITEM":
        add_to_inventory(engine.player_character.inventory, random_item(ITEMS))
        engine.board.tiles[engine.board.player_tile_position[0]][
                           engine.board.player_tile_position[1]].tile_type = "EMPTY"
    else:
        print("There is nothing here.")


def display_help():
    print("This is what you can do:\n"
          "move -> w / s / a / d\n"
          "check your stats -> c\n"
          "check you inventory -> i\n"
          "pick up items -> p\n"
          "quit the game -> q")


if __name__ == '__main__':
    main()

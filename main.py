import util
import game
from weapons_armor_items import weapons, weapon_names, armors, armor_names, powerups, powerups_names
from inventory import print_table, add_to_inventory, remove_from_inventory, random_item, ITEMS


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
            equip(engine)
        elif player_move == "u":
            use_item(engine)
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


def equip(engine):
    user_input = input("What would you like to equip?: ")
    if user_input in weapon_names and user_input in engine.player_character.inventory.keys():
        for i in range(len(weapon_names)):
            if user_input == weapon_names[i]:
                add_to_inventory(engine.player_character.inventory, [engine.player_character.weapon.name])
                engine.player_character.weapon = weapons[i]
                engine.player_character.update_attack()
    elif user_input in armor_names and user_input in engine.player_character.inventory.keys():
        for i in range(len(armor_names)):
            if user_input == armor_names[i]:
                if armors[i].body_part == "head":
                    add_to_inventory(engine.player_character.inventory, [engine.player_character.head.name])
                    engine.player_character.head = armors[i]
                elif armors[i].body_part == "torso":
                    add_to_inventory(engine.player_character.inventory, [engine.player_character.torso.name])
                    engine.player_character.torso = armors[i]
                elif armors[i].body_part == "arms":
                    add_to_inventory(engine.player_character.inventory, [engine.player_character.arms.name])
                    engine.player_character.arms = armors[i]
                elif armors[i].body_part == "legs":
                    add_to_inventory(engine.player_character.inventory, [engine.player_character.legs.name])
                    engine.player_character.legs = armors[i]
                elif armors[i].body_part == "shield":
                    add_to_inventory(engine.player_character.inventory, [engine.player_character.shield.name])
                    engine.player_character.shield = armors[i]
            engine.player_character.update_armor()
    else:
        print(f"You cannot equip {user_input}.")


def use_item(engine):
    user_input = input("What item would you like to use?: ")
    if user_input in engine.player_character.inventory.keys():
        if user_input == "Health potion":
            remove_from_inventory(engine.player_character.inventory, ["Health potion"])
            engine.player_character.heal_hp()
        elif user_input == "Mana potion":
            remove_from_inventory(engine.player_character.inventory, ["Mana potion"])
            engine.player_character.heal_mana()
        else:
            print(f"You cannot use {user_input}.")


def display_help():
    print("This is what you can do:\n"
          "move -> w / s / a / d\n"
          "check your stats -> c\n"
          "check you inventory -> i\n"
          "pick up items -> p\n"
          "equip various weapons and armor -> e"
          "use items -> u"
          "quit the game -> q")


if __name__ == '__main__':
    main()

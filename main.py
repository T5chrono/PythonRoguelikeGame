import os
import util
import game
import ui
from weapons_armor_items import weapons, weapon_names, armors, armor_names, powerups, powerups_names
from inventory import print_table, add_to_inventory, remove_from_inventory, random_item, ITEMS
from pygame import mixer

SUPPORTED_KEYS = {
    "Player movement": ["w", "s", "a", "d"],
    "Character details": "c",
    "Inventory": "i",
    "Pick up sth": "p",
    "Equip sth": "e",
    "Open equipment": "o",
    "Use sth": "u",
    "Quit": "q",
    "Help": "h"
}

MUSIC_FILE = "101-opening.wav"


def main():
    board_created = False

    util.clear_screen()
    # add music
    mixer.init()
    mixer.music.load(os.getcwd() + "/" + MUSIC_FILE)

    character_name = ui.get_character_name()

    while not board_created:
        try:
            engine = game.Game(character_name)
        except TypeError:
            print("Enter a number!")
        else:
            board_created = True

    # engine.board.display_board()

    # play music
    mixer.music.play()

    engine.is_running = True
    player_move = 'h'
    while player_move != SUPPORTED_KEYS['Quit'] and engine.is_running:
        if player_move in SUPPORTED_KEYS['Player movement']:
            engine.handle_movement_effects(player_move)
        elif player_move == SUPPORTED_KEYS['Character details']:
            get_char_details(engine)
        elif player_move == SUPPORTED_KEYS['Help']:
            get_help(engine)
        elif player_move == SUPPORTED_KEYS['Inventory']:
            get_inventory(engine)
        elif player_move == SUPPORTED_KEYS['Pick up sth']:
            pick_up_something(engine)
        elif player_move == SUPPORTED_KEYS['Equip sth']:
            equip(engine)
        elif player_move == SUPPORTED_KEYS['Use sth']:
            use_item(engine)
        elif player_move == SUPPORTED_KEYS['Open equipment']:
            print(engine.player_character)
        elif player_move == SUPPORTED_KEYS["distribute exp points"]:
            engine.player_character.distribute_points()
            engine.display_after_key_press()
        player_move = util.key_pressed()
    else:
        ui.display_goodbye(engine.player_character.name)


# clean up screen when you display info
def get_help(engine):
    util.clear_screen()
    engine.board.display_board()
    ui.display_help(**SUPPORTED_KEYS)


def get_char_details(engine):
    util.clear_screen()
    engine.board.display_board()
    ui.display_character_details(**engine.player_character.__dict__)


def get_inventory(engine):
    util.clear_screen()
    engine.board.display_board()
    print_table(engine.player_character.inventory)


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
                engine.player_character.weapon = weapons[i]
                engine.player_character.update_attack()
    elif user_input in armor_names and user_input in engine.player_character.inventory.keys():
        for i in range(len(armor_names)):
            if user_input == armor_names[i]:
                if armors[i].body_part == "head":
                    engine.player_character.head = armors[i]
                elif armors[i].body_part == "torso":
                    engine.player_character.torso = armors[i]
                elif armors[i].body_part == "arms":
                    engine.player_character.arms = armors[i]
                elif armors[i].body_part == "legs":
                    engine.player_character.legs = armors[i]
                elif armors[i].body_part == "shield":
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


if __name__ == '__main__':
    main()

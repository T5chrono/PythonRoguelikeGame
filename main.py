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
<<<<<<< HEAD
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
=======
        elif player_move == SUPPORTED_KEYS['character details']:
            engine.get_char_details()
        elif player_move == SUPPORTED_KEYS['help']:
            engine.get_help(SUPPORTED_KEYS)
        elif player_move == SUPPORTED_KEYS['inventory']:
            engine.get_inventory()
        elif player_move == SUPPORTED_KEYS['pick up sth']:
            engine.pick_up_something()
        elif player_move == SUPPORTED_KEYS['equip sth']:
            engine.equip()
        elif player_move == SUPPORTED_KEYS['use sth']:
            engine.use_item()
>>>>>>> bf60af87f3b471725d437d70b4d4a31421bf6b3c
        elif player_move == SUPPORTED_KEYS["distribute exp points"]:
            engine.player_character.distribute_points()
            engine.display_after_key_press()
        player_move = util.key_pressed()
    else:
        ui.display_goodbye(engine.player_character.name)


if __name__ == '__main__':
    main()

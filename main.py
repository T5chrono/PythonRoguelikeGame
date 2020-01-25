import os
import util
import game
import ui
from weapons_armor_items import weapons, weapon_names, armors, armor_names, powerups, powerups_names
from inventory import print_table, add_to_inventory, remove_from_inventory, random_item, ITEMS
from pygame import mixer

SUPPORTED_KEYS = {
    "player movement": ["w", "s", "a", "d"],
    "character details": "c",
    "inventory": "i",
    "pick up sth": "p",
    "equip sth": "e",
    "use sth": "u",
    "quit": "q",
    "help": "h",
    "distribute exp points": "l",
}

MUSIC_FILE = "music.wav"


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

    util.clear_screen()
    engine.board.display_board()
    # ui.display_help(**SUPPORTED_KEYS)

    # play music
    mixer.music.play()

    engine.is_running = True
    player_move = 'h'
    while player_move != SUPPORTED_KEYS['quit'] and engine.is_running:
        if player_move in SUPPORTED_KEYS['player movement']:
            engine.handle_movement_effects(player_move)
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
        elif player_move == SUPPORTED_KEYS["distribute exp points"]:
            engine.player_character.distribute_points()
            engine.display_after_key_press()
        player_move = util.key_pressed()
    else:
        ui.display_goodbye()


if __name__ == '__main__':
    main()

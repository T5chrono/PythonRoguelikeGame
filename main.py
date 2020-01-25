import util
import game
import ui
import sounds
import colors


SUPPORTED_KEYS = {
    "Player movement": ["w", "s", "a", "d"],
    "Character details": "c",
    "Inventory": "i",
    "Pick up sth": "p",
    "Equip sth": "e",
    "Use sth": "u",
    "Quit": "q",
    "Help": "h",
    "Distribute exp points": "l",
    "Examine the item": "x"
}


def main():
    board_created = False

    util.clear_screen()

    character_name = ui.get_user_value("\nPlease provide the name of your character! ", "Keanu")
    while not board_created:
        try:
            engine = game.Game(character_name)
        except TypeError:
            print(f"{colors.ERROR}Enter a number!{colors.RESET}")
        else:
            board_created = True
    engine.initialize_player_class_and_race()
    engine.is_running = True
    player_move = 'h'
    while player_move != SUPPORTED_KEYS['Quit'] and engine.is_running:
        if player_move in SUPPORTED_KEYS['Player movement']:
            engine.handle_movement_effects(player_move)
        elif player_move == SUPPORTED_KEYS['Character details']:
            engine.get_char_details()
        elif player_move == SUPPORTED_KEYS['Help']:
            engine.get_help(**SUPPORTED_KEYS)
        elif player_move == SUPPORTED_KEYS['Inventory']:
            engine.get_inventory()
        elif player_move == SUPPORTED_KEYS['Pick up sth']:
            engine.pick_up_something()
        elif player_move == SUPPORTED_KEYS['Equip sth']:
            engine.equip()
        elif player_move == SUPPORTED_KEYS['Use sth']:
            engine.use_item()
        elif player_move == SUPPORTED_KEYS["Distribute exp points"]:
            engine.player_character.distribute_points()
            engine.display_after_key_press()
        elif player_move == SUPPORTED_KEYS["Examine the item"]:
            engine.examine_item()
        player_move = util.key_pressed()
    else:
        ui.display_goodbye(engine.player_character.name)


if __name__ == '__main__':
    main()

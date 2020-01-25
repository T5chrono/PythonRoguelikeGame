import board
import util
import battle
import character
import ui
import colors
from weapons_armor_items import weapons, weapon_names, armors, armor_names, powerups, powerups_names, common_items, \
    common_items_names
import events
from inventory import print_table, add_to_inventory, remove_from_inventory, random_item, ITEMS


class Game():

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
    "Examine the item": "x"}

    def __init__(self, character_name="Keanu"):
        self.is_running = True

    def create_new_board(self):
        self.board = board.Board(Game.initialize_board(self, "height"), Game.initialize_board(self, "width"))
    
    def create_character(self, character_name):
        self.player_character = character.Character(character_name)

    def handle_actions(self):
        player_move = util.key_pressed()

        if player_move in Game.SUPPORTED_KEYS['Player movement']:
            self.handle_movement_effects(player_move)
        elif player_move == Game.SUPPORTED_KEYS['Character details']:
            self.get_char_details()
        elif player_move == Game.SUPPORTED_KEYS['Help']:
            self.get_help(**Game.SUPPORTED_KEYS)
        elif player_move == Game.SUPPORTED_KEYS['Inventory']:
            self.get_inventory()
        elif player_move == Game.SUPPORTED_KEYS['Pick up sth']:
            self.pick_up_something()
        elif player_move == Game.SUPPORTED_KEYS['Equip sth']:
            self.equip()
        elif player_move == Game.SUPPORTED_KEYS['Use sth']:
            self.use_item()
        elif player_move == Game.SUPPORTED_KEYS["Distribute exp points"]:
            self.player_character.distribute_points()
            self.display_after_key_press()
        elif player_move == Game.SUPPORTED_KEYS["Examine the item"]:
            self.examine_item()
        elif player_move == Game.SUPPORTED_KEYS["Quit"]:
            self.is_running = False

    def initialize_board(self, dimension):

        dimension_size = 0

        while dimension_size < 1 or dimension_size > 5:
            user_answer = input("Choose {} of map between 1 and 5: ".format(dimension))
            try:
                dimension_size = int(user_answer)
            except:
                raise TypeError("Enter a number!")

        return dimension_size

    def handle_movement_effects(self, player_move):
        try:
            new_position = self.board.get_new_index_of_position(player_move)
            if self.board.check_if_valid_move(new_position):
                if self.board.check_if_monster(new_position):
                    self.handle_entire_battle(new_position)

                elif self.board.check_if_item(new_position):
                    self.move(new_position)
                    print("There is " + colors.ITEM + "something" + colors.RESET + " here. Do you want to pick it up? (press '" + colors.ACTION + "p" + colors.RESET + "')")

                elif self.board.check_if_event(new_position):
                    self.move(new_position)
                    self.handle_event_effects(new_position)

                elif self.board.check_if_gate(new_position):
                    user_input = input("Do you want to enter the gate: ")
                    if user_input == 'y':
                        if self.board.board_level < 2:
                            self.board.generate_new_board()
                        else:
                            self.board.generate_boss_level()

                else:
                    self.move(new_position)
                    self.board.place_random_monster()

        except IndexError:
            util.clear_screen()
            self.board.display_board()
            print("You can't move on wall!")

    def move(self, new_position):
        self.board.move_player(new_position)
        util.clear_screen()
        self.board.display_board()
        if self.board.is_boss:
            self.board.move_boss()
        print(self.board.tiles[new_position[0]][new_position[1]].descirption)

    def handle_event_effects(self, new_position):
        event = events.Event.get_random_event()
        self.player_character.strength += event.strenght
        self.player_character.current_hp += event.hp
        self.player_character.dexterity += event.dexterity
        self.player_character.intelligence += event.intelligence
        self.player_character.current_experience += event.exp
        self.player_character.correct_current_hp_to_max()
        self.player_character.check_if_lvl_up()
        self.board.make_tile_empty(new_position)
        self.is_running = self.player_character.current_hp > 0
        print(event.description)

    def handle_entire_battle(self, new_position):
        fight = battle.Battle(self.player_character)
        print("You meet {}". format(colors.ENEMY + str(fight.monster.name) + colors.RESET))
        is_figthing = True

        while is_figthing:
            is_figthing = fight.handle_fight_round()
            self.is_running = (self.player_character.current_hp > 0)

        if fight.monster_hp < 1:
            self.board.make_tile_empty(new_position)
            self.player_character.check_if_lvl_up()
            self.board.place_item(new_position)
        if self.is_running:
            self.display_after_key_press()

    def display_after_key_press(self):
        print("Press any key to continue")
        util.key_pressed()
        util.clear_screen()
        self.board.display_board()

    def get_help(self, **SUPPORTED_KEYS):
        util.clear_screen()
        self.board.display_board()
        ui.display_help(**SUPPORTED_KEYS)

    def get_char_details(self):
        util.clear_screen()
        self.board.display_board()
        print(self.player_character)

    def get_inventory(self):
        util.clear_screen()
        self.board.display_board()
        print_table(self.player_character.inventory)

    def equip(self):
        user_input = input("What would you like to equip?: ")
        if user_input in weapon_names and user_input in self.player_character.inventory.keys():
            for i in range(len(weapon_names)):
                if user_input == weapon_names[i]:
                    self.player_character.weapon = weapons[i]
                    self.player_character.update_attack()
        elif user_input in armor_names and user_input in self.player_character.inventory.keys():
            for i in range(len(armor_names)):
                if user_input == armor_names[i]:
                    if armors[i].body_part == "head":
                        self.player_character.head = armors[i]
                    elif armors[i].body_part == "torso":
                        self.player_character.torso = armors[i]
                    elif armors[i].body_part == "arms":
                        self.player_character.arms = armors[i]
                    elif armors[i].body_part == "legs":
                        self.player_character.legs = armors[i]
                    elif armors[i].body_part == "shield":
                        self.player_character.shield = armors[i]
                self.player_character.update_armor()
        else:
            print(f"You cannot equip {user_input}.")

    def use_item(self):
        user_input = input("What item would you like to use?: ")
        if user_input in self.player_character.inventory.keys():
            if user_input == "Health potion":
                remove_from_inventory(self.player_character.inventory, ["Health potion"])
                self.player_character.heal_hp()
        elif user_input == "Mana potion":
            remove_from_inventory(self.player_character.inventory, ["Mana potion"])
            self.player_character.heal_mana()
        elif not user_input:
            print("You cannot equip nothing.")
        else:
            print(f"You cannot use {user_input}.")

    def examine_item(self):
        user_input = input("What item would you like to examine?: ")
        if user_input in self.player_character.inventory.keys():
            if user_input in weapon_names:
                for i in range(len(weapon_names)):
                    if user_input == weapon_names[i]:
                        print(f"{weapons[i].status} (Attack: + {weapons[i].attack}).")
            elif user_input in armor_names:
                for i in range(len(armor_names)):
                    if user_input == armor_names[i]:
                        print(f"{armors[i].status} (Armor: + {armors[i].armor}).")
            elif user_input in powerups_names:
                for i in range(len(powerups_names)):
                    if user_input == powerups_names[i]:
                        print(powerups[i].status)
            elif user_input in common_items_names:
                for i in range(len(common_items_names)):
                    if user_input == common_items_names[i]:
                        print(common_items[i].status)
        elif not user_input:
            print("You cannot examine nothing.")
        else:
            print(f"You cannot examine {user_input}.")

    def pick_up_something(self):
        if self.board.tiles[self.board.player_tile_position[0]][
            self.board.player_tile_position[1]].tile_type == "ITEM":
            add_to_inventory(self.player_character.inventory, random_item(ITEMS))
            self.board.tiles[self.board.player_tile_position[0]][
                self.board.player_tile_position[1]].tile_type = "EMPTY"
        else:
            print("There is nothing here.")

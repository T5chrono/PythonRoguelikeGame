import board
import util
import battle
import character
import colors
import ui
import events
import weapons
import armors
import items
import powerups
import boss

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

    PLAYER_STATS = "."

    def __init__(self):
        self.boss = boss.Boss()
        self.is_running = True
        self.player_character = character.Character()
        self.UI = ui.GameUI(self)

    def create_new_board(self):
        self.board = board.Board(self.get_board_dimension("height"), self.get_board_dimension("width"))
    
    def add_character_name(self, character_name):
        self.player_character.name = character_name

    def initialize_player_class_and_race(self):
        player_race, player_class = self.player_character.get_character_type()
        self.player_character.add_character_type((player_race, player_class))

    def handle_action(self):
        player_move = util.key_pressed()

        if player_move in Game.SUPPORTED_KEYS['Player movement']:
            self.handle_movement_effects(player_move)
        elif player_move == Game.SUPPORTED_KEYS['Character details']:
            self.UI.display_char_details()
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
            self.UI.display_board_after_key_press()
        elif player_move == Game.SUPPORTED_KEYS["Examine the item"]:
            self.examine_item()
        elif player_move == Game.PLAYER_STATS:
            self.player_character.ui.display_dict_details("\n Player stats:\n", **self.player_character.__dict__)
        elif player_move == Game.SUPPORTED_KEYS["Quit"]:
            self.is_running = False
        elif player_move == "f":
            self.say()

    def get_board_dimension(self, dimension):

        dimension_size = 0

        while dimension_size < 1 or dimension_size > 5:
            user_answer = input("Choose {} of map between {}1 and 5{}: ".format(dimension, colors.ACTION, colors.RESET))
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
                    self.UI.display_info_item()

                elif self.board.check_if_event(new_position):
                    self.move(new_position)
                    self.handle_event_effects(new_position)

                elif self.board.check_if_gate(new_position):
                    user_input = input(ui.GameUI.GATE_INFO)
                    if user_input.lower() == 'y':
                        if self.board.board_level <= 1:
                            self.board.generate_new_board()
                            util.clear_screen()
                            self.board.display_board()
                        else:
                            self.board.generate_boss_level()
                            util.clear_screen()
                            self.board.display_board()

                elif self.board.check_if_boss(new_position):
                    print("Boss is here")
                    self.handle_boss_battle()

                else:
                    self.move(new_position)

        except IndexError:
            self.UI.display_board()
            self.UI.display_error_info("out of index")

    def move(self, new_position):
        self.board.move_player(new_position)
        self.UI.display_board()
        if self.board.is_boss:
            self.board.move_boss()
        print(self.board.tiles[new_position[0]][new_position[1]].descirption)
        self.board.place_random_monster()

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
        self.UI.display_monster_info(fight.monster.name)
        is_figthing = True

        while is_figthing:
            is_figthing = fight.handle_fight_round()
            self.is_running = (self.player_character.current_hp > 0)

        if fight.monster_hp < 1:
            self.board.make_tile_empty(new_position)
            self.player_character.check_if_lvl_up()
            self.board.place_item(new_position)
        if self.is_running:
            self.UI.display_board_after_key_press()

    def get_inventory(self):
        self.UI.display_board()
        self.player_character.inventory.print_table()

    def equip(self):
        user_input = input(ui.GameUI.EQUIP_QUESTION)
        if user_input in weapons.WeaponsPool.weapon_names and user_input in self.player_character.inventory.items.keys():
            for i in range(len(weapons.WeaponsPool.weapon_names)):
                if user_input == weapons.WeaponsPool.weapon_names[i]:
                    self.player_character.weapon = weapons.WeaponsPool.weapons[i]
                    self.player_character.update_attack()
        elif user_input in armors.ArmorsPool.armor_names and user_input in self.player_character.inventory.items.keys():
            for i in range(len(armors.ArmorsPool.armor_names)):
                if user_input == armors.ArmorsPool.armor_names[i]:
                    if armors.ArmorsPool.armors[i].body_part == "head":
                        self.player_character.head = armors.ArmorsPool.armors[i]
                    elif armors.ArmorsPool.armors[i].body_part == "torso":
                        self.player_character.torso = armors.ArmorsPool.armors[i]
                    elif armors.ArmorsPool.armors[i].body_part == "arms":
                        self.player_character.arms = armors.ArmorsPool.armors[i]
                    elif armors.ArmorsPool.armors[i].body_part == "legs":
                        self.player_character.legs = armors.ArmorsPool.armors[i]
                    elif armors.ArmorsPool.armors[i].body_part == "shield":
                        self.player_character.shield = armors.ArmorsPool.armors[i]
                self.player_character.update_armor()
        else:
            self.UI.display_error_info("wrong item")

    def use_item(self):
        user_input = input(ui.GameUI.USE_QUESTION)
        if user_input in self.player_character.inventory.items.keys():
            if user_input == "Health potion":
                self.player_character.inventory.remove_from_inventory(user_input)
                self.player_character.heal_hp()
            elif user_input == "Mana potion":
                self.player_character.inventory.remove_from_inventory(user_input)
                self.player_character.heal_mana()
            else:
                self.UI.display_error_info("wrong item")
        elif not user_input:
            self.UI.display_error_info("no item")
        

    def examine_item(self):
        user_input = input(ui.GameUI.EXAMINE_ITEM)
        if user_input in self.player_character.inventory.items.keys():
            if user_input in weapons.WeaponsPool.weapon_names:
                for i in range(len(weapons.WeaponsPool.weapon_names)):
                    if user_input == weapons.WeaponsPool.weapon_names[i]:
                        print(f"{weapons.WeaponsPool.weapons[i].status} (Attack: + {weapons.WeaponsPool.weapons[i].attack}).")
            elif user_input in armors.ArmorsPool.armor_names:
                for i in range(len(armors.ArmorsPool.armor_names)):
                    if user_input == armors.ArmorsPool.armor_names[i]:
                        print(f"{armors.ArmorsPool.armors[i].status} (Armor: + {armors.ArmorsPool.armors[i].armor}).")
            elif user_input in powerups.PowerUpsPool.powerups_names:
                for i in range(len(powerups.PowerUpsPool.powerups_names)):
                    if user_input == powerups.PowerUpsPool.powerups_names[i]:
                        print(powerups.PowerUpsPool.powerups[i].status)
            elif user_input in items.CommonItemsPool.common_items_names:
                for i in range(len(items.CommonItemsPool.common_items_names)):
                    if user_input == items.CommonItemsPool.common_items_names[i]:
                        print(items.CommonItemsPool.common_items[i].status)
        elif not user_input:
            self.UI.display_error_info("no item")
        else:
            self.UI.display_error_info("wrong item")

    def pick_up_something(self):
        if self.board.check_if_current_tile_is_item():
            self.player_character.inventory.add_to_inventory()
            self.board.make_tile_empty(self.board.player_tile_position)
        else:
            self.UI.display_error_info("empty tile")

    def say(self):
        user_input = input(ui.UI.SAY_QUESTION)
        if user_input == "Fork yourself":
            pass
        else:
            print("No one cares!")

    def handle_boss_battle(self):
        question1 = "Aaa, it's you! Where is my report.\n 1. My dog ate it.\n 2. I will bring it tomorrow.\n " \
                    "3. I don't care about your report! Let's fight.\n "
        question2 = "I need it now!\n 1. Time is just a construct.\n 2. Maybe I can offer you something else?\n " \
                    "3. I don't care about your report. Let's fight.\n "
        question3 = "What do you have in mind?\n 1. Let's just forget about it? \n 2. Maybe you want a cake?\n " \
                    "3. I don't care about your report. Let's fight.\n "
        ui.UI.print_message(question1)
        user_input = self.user_answer()
        if user_input == '1':
            self.you_are_fired()
        elif user_input == '2':
            ui.UI.print_message(question2)
            user_input = self.user_answer()
            if user_input == '1':
                self.you_are_fired()
            elif user_input == '2':
                ui.UI.print_message(question3)
                user_input = self.user_answer()
                if user_input == '1':
                    self.you_are_fired()
                elif user_input == '2':
                    self.you_get_a_promotion()
                elif user_input == '3':
                    self.fight_with_boss()
                else:
                    self.remind_player_to_say_something()
            elif user_input == '3':
                self.fight_with_boss()
            else:
                self.remind_player_to_say_something()
        elif user_input == '3':
            self.fight_with_boss()
        else:
            self.remind_player_to_say_something()

    def user_answer(self):
        return input("What is your answer?: ")

    def remind_player_to_say_something(self):
        ui.UI.print_message("You have to answer somehow ('1', '2' or '3')")

    def you_are_fired(self):
        ui.UI.print_message("You are fired!!! ")
        ui.UI.print_message("Congratualtions. You reached negative ending")
        self.is_running = False
        # TODO: negative end game screen

    def you_get_a_promotion(self):
        ui.UI.print_message("Well I guess it is ok. \n I will give you a promotion")
        ui.UI.print_message("Congratualtions. You reached positive ending")
        self.is_running = False
        # TODO positive end game screen

    def fight_with_boss(self):
        boss_fight = boss.BossBattle(self.player_character)
        self.UI.display_monster_info(self.boss.name)
        is_fighting = True

        while is_fighting:
            is_fighting = boss_fight.handle_fight_round()
            self.is_running = (self.player_character.current_hp > 0)

        if boss_fight.boss_hp < 1:
            self.you_get_a_promotion()
        if self.is_running:
            self.UI.display_board_after_key_press()

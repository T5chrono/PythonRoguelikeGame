import colors
import game
import util
import os
import time


IMAGES_DIRECTORY = os.getcwd() +"/images/"
OPENING_FILE = "START"
WIN_FILE = "WIN"
RIP_FILE = "RIP"
INFO, ERROR = range(2)


class UI():
    PROVIDE_NAME = "\nPlease provide the name of your character! "

    def get_user_value(self, info_message, default_value):
        player_value = input(colors.PLAYER + info_message + colors.RESET)
        return player_value if player_value else default_value

    def display_message(self, info_message, message_type = INFO):
        if message_type == ERROR:
            print(f"\n{colors.ERROR}{info_message}{colors.RESET}\n")
        else:
            print(f"\n{colors.INFO}{info_message}{colors.RESET}\n")

    def display_list_details(self, info_message, *args):
        print(f"\n{colors.INFO}{info_message}{colors.RESET}{colors.ACTION}")
        print(*args, sep=colors.RESET + ", " + colors.ACTION, end=colors.RESET + "\n")


    def display_dict_details(self, info_message, **kwargs):
        print(info_message)
        for k, v in kwargs.items():
            if not self.is_instance_userdefined_and_newclass(v) and v:
                print(f"{k}: {v}")

    def is_instance_userdefined_and_newclass(self, inst):
        cls = inst.__class__
        if hasattr(cls, '__class__'):
            return ('__dict__' in dir(cls) or hasattr(cls, '__slots__'))
        return False

    def print_message(something):
        print(something)

    # displays open title and RIP
    def display_by_line(file_path):
        delay_time = 0.3
        os.system("clear")
        with open(file_path) as fp:
            for line in fp:
                time.sleep(delay_time)
                print(line, end="")


class GameUI():

    GATE_INFO = f"\n{colors.GATE}Do you want to enter the gate? (y/n) {colors.RESET}"
    NUMBER_ERROR = f"{colors.ERROR}Enter a number!{colors.RESET}"
    WALL_WARNING = f"{colors.ACTION}You can't move on wall!{colors.RESET}"
    EQUIP_QUESTION = "What would you like to equip?: "
    USE_QUESTION = "What item would you like to use?: "
    WRONG_ITEM = "You cannot do that!"
    NO_ITEM_CHOSE = "You cannot do that with nothing."
    EXAMINE_ITEM = "What item would you like to examine?: "
    EMPTY_TILE = "There is nothing here."
    SAY_QUESTION = "What do you want to say?: "

    def __init__(self, game):
        self.game_engine = game

    def display_error_info(self, error_type):
        if error_type == "expected number":
            print(GameUI.NUMBER_ERROR)
        elif error_type == "out of index":
            print(GameUI.WALL_WARNING)
        elif error_type == "wrong item":
            print(GameUI.WRONG_ITEM)
        elif error_type == "no item":
            print(GameUI.NO_ITEM_CHOSE)
        elif error_type == "empty tile":
            print(GameUI.EMPTY_TILE)


    def display_char_details(self):
        self.display_board()
        print(self.game_engine.player_character)

    def display_monster_info(self, monster_name):
        print("\nYou meet {}\n". format(colors.ENEMY + monster_name + colors.RESET))

    def display_board_after_key_press(self):
        print("Press any key to continue")
        util.key_pressed()
        self.display_board()

    def display_board(self):
        util.clear_screen()
        self.game_engine.board.display_board()

    def display_help(self):
        self.display_board()
        print(f"\n{colors.INFO}Please find available options below!{colors.RESET}\n")
        for k, v in game.Game.SUPPORTED_KEYS.items():
            if isinstance(v, list):
                print(f"{colors.ACTION}{k}{colors.RESET} -> Press one from: '{colors.INFO}", end="")
                print(*v, sep=colors.RESET+"'/'"+colors.INFO, end=colors.RESET+"'\n")
            else:
                print(f"{colors.ACTION}{k}{colors.RESET} -> Press '{colors.INFO}{v}{colors.RESET}'")

    def display_goodbye(self):
        print(f"\n{colors.PLAYER}Bye {colors.RESET}{colors.ENEMY}{self.game_engine.player_character.name}{colors.RESET}{colors.PLAYER}! Thanks for playing!{colors.RESET}\n")

    def display_info_item(self):
        print("\nThere is " + colors.ITEM + "something" + colors.RESET + " here. \nDo you want to pick it up? (press '" + colors.ACTION + "p" + colors.RESET + "')")


# to be modified after inventory Class
def display_added_item(*args):
    print("\nCongratulations! You found " + colors.PLAYER, *args, colors.RESET + "!", sep="")

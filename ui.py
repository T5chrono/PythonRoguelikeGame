import colors
import game
import util

INFO, ERROR = range(2)

class UI():

    GATE_INFO = f"\n{colors.GATE}Do you want to enter the gate? (y/n) {colors.RESET}"
    NUMBER_ERROR = f"{colors.ERROR}Enter a number!{colors.RESET}"
    PROVIDE_NAME = "Please provide the name of your character! "
    WALL_WARNING = f"{colors.ACTION}You can't move on wall!{colors.RESET}"

    def __init__(self, game):
        self.game_engine = game

    def display_error_info(self, error_type):
        if error_type == "expected number":
            print(UI.NUMBER_ERROR)
        elif error_type == "out of index":
            print(UI.WALL_WARNING)

    def display_monster_info(self, monster_name):
        print("\nYou meet {}\n". format(colors.ENEMY + monster_name + colors.RESET))

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

    
def get_user_value(info_message, default_value):
    player_value = input(colors.PLAYER + info_message + colors.RESET)
    return player_value if player_value else default_value


def display_message(info_message, message_type = INFO):
    if message_type == ERROR:
        print(f"\n{colors.ERROR}{info_message}{colors.RESET}\n")
    else:
        print(f"\n{colors.INFO}{info_message}{colors.RESET}\n")


def display_help(**kwargs):
    print(f"\n{colors.INFO}Please find available options below!{colors.RESET}\n")
    for k, v in kwargs.items():
        if isinstance(v, list):
            print(f"{colors.ACTION}{k}{colors.RESET} -> Press one from: '{colors.INFO}", end="")
            print(*v, sep=colors.RESET+"'/'"+colors.INFO, end=colors.RESET+"'\n")
        else:
            print(f"{colors.ACTION}{k}{colors.RESET} -> Press '{colors.INFO}{v}{colors.RESET}'")


def display_list_details(info_message, *args):
    print(f"\n{colors.INFO}{info_message}{colors.RESET}{colors.ACTION}")
    print(*args, sep=colors.RESET + ", " + colors.ACTION, end=colors.RESET + "\n")


def display_dict_details(info_message, **kwargs):
    print(info_message)
    for k, v in kwargs.items():
        if not is_instance_userdefined_and_newclass(v) and v:
            print(f"{k}: {v}")


def is_instance_userdefined_and_newclass(inst):
    cls = inst.__class__
    if hasattr(cls, '__class__'):
        return ('__dict__' in dir(cls) or hasattr(cls, '__slots__'))
    return False


def display_added_item(*args):
    print("\nCongratulations! You found " + colors.PLAYER, *args, colors.RESET + "!", sep="")


def display_goodbye(player_name):
    print(f"\n{colors.PLAYER}Bye {colors.RESET}{colors.ENEMY}{player_name}{colors.RESET}{colors.PLAYER}! Thanks for playing!{colors.RESET}\n")

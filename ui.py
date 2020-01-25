def get_character_name():
    name = input("Please provide the name of your character! :) ")
    return name if name != "" else "Keanu"


def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''

    # engine.board.display_board()
    pass


def display_help(**kwargs):
    print("\nPlease find available options below!\n")
    for k, v in kwargs.items():
        if isinstance(v, list):
            print(f"{k} -> Press one from: '", end="")
            print(*v, sep="'/'", end="'\n")
        else:
            print(f"{k} -> Press '{v}'")


def display_character_details(**kwargs):
    print("\nPlease find details of your hero below!")
    for k, v in kwargs.items():
        if not is_instance_userdefined_and_newclass(v) and v:
            print(f"{k}: {v}")


def is_instance_userdefined_and_newclass(inst):
    cls = inst.__class__
    if hasattr(cls, '__class__'):
        return ('__dict__' in dir(cls) or hasattr(cls, '__slots__'))
    return False


def display_added_item(*args):
    print("Congratulations! You found ", *args, "!", sep="")


def display_goodbye(player_name):
    print(f"\nBye {player_name}! Thanks for playing!")

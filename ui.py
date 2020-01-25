def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''

    # engine.board.display_board()
    pass


def display_character_details(**kwargs):
    print("Please find details of your hero below!")
    for k, v in kwargs.items():
        if not is_instance_userdefined_and_newclass(v) and v:
            print(f"{k}: {v}")


def is_instance_userdefined_and_newclass(inst):
    cls = inst.__class__
    if hasattr(cls, '__class__'):
        return ('__dict__' in dir(cls) or hasattr(cls, '__slots__'))
    return False

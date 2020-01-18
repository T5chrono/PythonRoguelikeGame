import board 

class Game():

    def __init__(self):
        self.board = board.Board(Game.initialize_board(self, "height"), Game.initialize_board(self, "width"))

    def initialize_board(self, dimension):

        dimension_size = 0

        while dimension_size < 1 or dimension_size > 5:
            user_answer = input("Choose {} of map between 1 and 5: ".format(dimension))
            try:
                dimension_size = int(user_answer)
            except:
                raise TypeError("Enter a number!")

        return dimension_size


import board
import util

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

    def handle_movement_effects(self, player_move):
        try:
            new_position = self.board.get_new_index_of_position(player_move)
            if self.board.check_if_valid_move(new_position):
                if self.board.check_if_monster(new_position):
                    print("Monster here!")
                elif self.board.check_if_item(new_position):
                    self.move(new_position)
                    print("There is something here.")
                else:
                    self.move(new_position)

        except IndexError:
            util.clear_screen()
            self.board.display_board()
            print("You can't move on wall!")

    def handle_item(self):
        if self.board.check_if_item():
            print("There is something here")


    def move(self, new_position):
        self.board.move_player(new_position)
        util.clear_screen()
        self.board.display_board()




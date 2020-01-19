import board
import util
import battle
import character

class Game():

    def __init__(self):
        self.is_running = True
        self.board = board.Board(Game.initialize_board(self, "height"), Game.initialize_board(self, "width"))
        self.player_character = character.Character("Keanu")

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
                    fight = battle.Battle(self.player_character)
                    print("You meet {}". format(fight.monster.name))
                    is_figthing = True
                    while is_figthing:
                        is_fighting = fight.handle_fight_round()
                        
                    self.is_running = (self.player_character.current_hp > 0)

                elif self.board.check_if_item(new_position):
                    self.move(new_position)
                    print("There is something here. Do you want to pick it up? (press \"p\")")
                else:
                    self.move(new_position)

        except IndexError:
            util.clear_screen()
            self.board.display_board()
            print("You can't move on wall!")

    def move(self, new_position):
        self.board.move_player(new_position)
        util.clear_screen()
        self.board.display_board()




import board
import util
import battle
import character


class Game():

    def __init__(self, character_name = "Keanu"):
        self.is_running = True
        self.board = board.Board(Game.initialize_board(self, "height"), Game.initialize_board(self, "width"))
        self.player_character = character.Character(character_name)

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

    def handle_entire_battle(self, new_position):
        fight = battle.Battle(self.player_character)
        print("You meet {}". format(fight.monster.name))
        is_figthing = True

        while is_figthing:
            is_figthing = fight.handle_fight_round()
            self.is_running = (self.player_character.current_hp > 0)

        if fight.monster_hp < 1:
            self.board.make_tile_empty(new_position)
        if self.is_running:
            self.display_after_key_press()

    def display_after_key_press(self):
        print("Press any key to continue")
        util.key_pressed()
        util.clear_screen()
        self.board.display_board()

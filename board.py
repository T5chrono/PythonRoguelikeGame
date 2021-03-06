import colors
from enum import Enum
from random import randint
from random import choice
from colored import fg, attr
import ui


class TileTypes(Enum):
    EMPTY = 1
    ITEM = 2
    MONSTER = 3
    EVENT = 4
    WALL = 5
    GATE = 6
    BOSS = 7


class Tile():

    places = ["You enter a ladies' toilet. It smells badly", "You ran into a desk and hurt your feet", "There is an empty conference room. You take a short nap", "You sit on a warm chair", "You see sleeping workers", "You hear dropping water",
             "A cleaning gentleman is walking with a vacuum", "You read some graphs about income", "You notice a teddy bear on the desk. You come closer to hug it",
             "You stop to play on Xbox", "You throw a PlayStation thru a window", "You look thru a window and see a car crash", "You noticed pills lying on the table but you cannot swallow them",
             "You split coffee on some important documents, but no one notices", "You notice a ping pong table. You stop to play for a minute... or a bit longer. Only a little bit.", "You found a knife and throw it randomly. You hear screams",
             "You ate an old sandwich and feel sick now", "You ran to the toilet quickly", "An old lady gave you an apple. You throw it away", "You slip on a banana skin... or human. Whatever", "The manager forgot to give you a promised promotion, but he sent you to ethics training to compensate",
             "You receive an email with pointless tasks, but you must do it immediately", "You report a broken window... after a month you get used to spikes of adrenaline when sitting nearby",
             "You wanted to report bugs, but it appears no one is responsible for fixing it", "Your cousin died? We are so sorry... NO! YOU CAN'T TAKE A DAY OFF!'",
             "The manager is thankful for your excellent work, but giving you a raise would ruin the entire company", "You have nothing to do, but you pretend you are busy to avoid being shout at",
             "You hide in a toilet"]



    def __init__(self, imported_type):
        self.is_player = False
        self.empty_tile_chance = 100
        self.monster_tile_chance = 4
        self.item_tile_chance = 3
        self.event_tile_chance = 2
        self.tile_type = Tile.determine_tile_type(self, imported_type)
        self.is_passable = Tile.is_passable(self)
        self.descirption = choice(Tile.places)

    def is_passable(self):
        if self.tile_type == "WALL":
            return False
        else:
            return True

    def determine_tile_type(self, imported_type):

        tiles_types = [".", "■"]

        if imported_type == tiles_types[0]:
            rng = randint(1, 100)
            if rng < self.event_tile_chance:
                return TileTypes.EVENT.name
            elif rng < self.item_tile_chance:
                return TileTypes.ITEM.name
            elif rng < self.monster_tile_chance:
                return TileTypes.MONSTER.name
            else:
                return TileTypes.EMPTY.name
        elif imported_type == tiles_types[1]:
            return TileTypes.WALL.name
        else:
            pass


class Board():

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.tiles = Board.make_board(self)
        self.player_tile_position = Board.place_player(self)
        self.gate_tile_position = Board.place_gate(self)
        self.board_level = 1
        self.is_boss = False

    def generate_new_board(self):
        self.tiles = self.make_board()
        self.player_tile_position = Board.place_player(self)
        self.gate_tile_position = Board.place_gate(self)
        self.board_level += 1

    def generate_boss_level(self):
        self.generate_new_board()
        self.place_boss()

    def get_random_map_path(self):
        rooms_number = 18
        random_number = randint(1, rooms_number)
        maps_path = "rooms/room"
        filename = maps_path + str(random_number)
        return filename

    def get_tiles_list_from_map_file(self):
        filename = Board.get_random_map_path(self)
        tiles_list = split_file_into_list(read_file(filename))
        return tiles_list

    def get_tile_index_to_move(self, direction, index):
        directions = ["w", "a", "s", "d"]

        if direction == directions[0]:
            index[0] -= 1
        elif direction == directions[1]:
            index[1] -= 1
        elif direction == directions[2]:
            index[0] += 1
        else:
            index[1] += 1
        return index

    def move_player(self, new_index):
        self.tiles[self.player_tile_position[0]][self.player_tile_position[1]].is_player = False
        self.tiles[new_index[0]][new_index[1]].is_player = True
        self.player_tile_position = new_index

    def check_if_monster(self, new_index):
        is_monster = (self.tiles[new_index[0]][new_index[1]].tile_type == "MONSTER")
        return is_monster

    def check_if_item(self, new_index):
        return self.tiles[new_index[0]][new_index[1]].tile_type == "ITEM"
    
    def check_if_current_tile_is_item(self):
        return self.tiles[self.player_tile_position[0]][self.player_tile_position[1]].tile_type == "ITEM"

    def check_if_event(self, index):
        if_event = self.tiles[index[0]][index[1]].tile_type == "EVENT"
        return if_event

    def check_if_gate(self, index):
        if_gate = self.tiles[index[0]][index[1]].tile_type == "GATE"
        return if_gate

    def check_if_boss(self, index):
        if_boss = self.tiles[index[0]][index[1]].tile_type == "BOSS"
        return if_boss

    def make_tile_empty(self, index):
        self.tiles[index[0]][index[1]].tile_type = TileTypes.EMPTY.name

    def get_new_index_of_position(self, direction):
        index = self.player_tile_position.copy()
        new_index = Board.get_tile_index_to_move(self, direction, index)
        return new_index

    def check_if_valid_move(self, new_index):
        is_valid = False

        try:
            new_tile = self.tiles[new_index[0]][new_index[1]]
        except:
            raise IndexError("You can't move on wall!")

        if new_index[0] < 0 or new_index[1] < 0:
            raise IndexError("You can't move on wall!")
        elif new_tile.is_passable:
            is_valid = True
        else:
            raise IndexError("You can't move on wall!")

        return is_valid

    def make_board(self):
        temp_width = 0
        # tiles_in_row = 30
        current_tiles = []

        while temp_width < self.width:
            temp_height = 0
            iteration = 0

            while temp_height < self.height:
                random_map = Board.get_tiles_list_from_map_file(self)

                for row in random_map:
                    if temp_width > 0:
                        tiles = current_tiles[iteration]
                    else:
                        tiles = []

                    for char in row:
                        tiles.append(Tile(char))

                    if temp_width > 0:
                        current_tiles[iteration] = tiles
                    else:
                        current_tiles.append(tiles)

                    iteration += 1
                temp_height += 1

            temp_width += 1

        return current_tiles

    def display_board(self):
        tiles_print_mapping = {
            "EMPTY": colors.EMPTY + "." + colors.RESET,
            "EVENT": colors.EVENT + "!" + colors.RESET,
            "MONSTER": colors.MONSTER + "X" + colors.RESET,
            "ITEM": colors.ITEM + "$" + colors.RESET,
            "WALL": colors.WALL + "#" + colors.RESET,
            "PLAYER": colors.PLAYER + "@" + colors.RESET,
            "GATE": colors.GATE + "G" + colors.RESET,
            "BOSS": colors.BOSS + "%" + colors.RESET,
            }
        board_width = len(self.tiles[0]) + 2
        edge = colors.WALL + "#" + colors.RESET

        print(board_width * edge)

        for row in self.tiles:
            row_to_print = edge
            for tile in row:
                if tile.is_player:
                    row_to_print += tiles_print_mapping["PLAYER"]
                else:
                    row_to_print += tiles_print_mapping[tile.tile_type]

            row_to_print += edge
            print(row_to_print)
        print(board_width * edge)

    def get_random_passable_position(self):
        incorrect_position = True
        random_passable_tile_index = []
        max_index_x = (self.width * 30) - 1
        max_index_y = (self.height * 10) - 1

        while incorrect_position:
            position_x = randint(0, max_index_x)
            position_y = randint(0, max_index_y)

            if self.tiles[position_y][position_x].tile_type != "BOSS" and self.tiles[position_y][position_x].is_passable and not self.tiles[position_y][position_x].is_player:
                random_passable_tile_index = [position_y, position_x]
                incorrect_position = False

        return random_passable_tile_index

    def place_gate(self):
        gate_index = Board.get_random_passable_position(self)
        self.tiles[gate_index[0]][gate_index[1]].tile_type = "GATE"
        return gate_index

    def place_player(self):
        player_index = Board.get_random_passable_position(self)
        self.tiles[player_index[0]][player_index[1]].is_player = True
        return player_index

    def place_random_monster(self):
        chances_to_spawn_monster = 10
        if randint(0, 100) < chances_to_spawn_monster:
            monster_index_corect = False
            while not monster_index_corect:
                 monster_index = self.get_random_passable_position()
                 if self.tiles[monster_index[0]][monster_index[1]].tile_type == "EMPTY":
                    self.tiles[monster_index[0]][monster_index[1]].tile_type = "MONSTER"
                    print(f"\n{colors.MONSTER}Oh no!! A new monster has arrived!{colors.RESET}")
                    monster_index_corect = True

    def place_item(self, new_position):
        chances_to_spawn_item = 20
        if randint(0, 100) < chances_to_spawn_item:
            self.tiles[new_position[0]][new_position[1]].tile_type = "ITEM"
            print("The monster dropped an item")

    def place_boss(self):
        self.boss_index = self.get_random_passable_position()
        boss_correct = 0
        for y in range(3):
            for x in range(3):
                if self.tiles[self.boss_index[0]+y][self.boss_index[1]+x].tile_type == "EMPTY" and self.tiles[self.boss_index[0]+y][self.boss_index[1]+x].is_player == False:
                    boss_correct += 1
        if boss_correct == 9:
            for y in range(3):
                for x in range(3):
                    self.tiles[self.boss_index[0]+y][self.boss_index[1]+x].tile_type = "BOSS"
            self.is_boss = True
        else:
            self.place_boss()

    def move_boss(self):
        temp_position = self.boss_index.copy()
        temp_position[0] += randint(-1, 1)
        temp_position[1] += randint(-1, 1)
        boss_correct = 0
        for y in range(3):
            for x in range(3):
                if (self.tiles[temp_position[0]+y][temp_position[1]+x].tile_type == "EMPTY" or self.tiles[temp_position[0]+y][temp_position[1]+x].tile_type == "BOSS") and self.tiles[self.boss_index[0]+y][self.boss_index[1]+x].is_player == False:
                    boss_correct += 1
        if boss_correct == 9:
            self.remove_boss()
            self.boss_index = temp_position.copy()
            for y in range(3):
                for x in range(3):
                    self.tiles[self.boss_index[0]+y][self.boss_index[1]+x].tile_type = "BOSS"
            print("The boss moved!")

    def remove_boss(self):
        for y in range(3):
            for x in range(3):
                self.tiles[self.boss_index[0]+y][self.boss_index[1]+x].tile_type = "EMPTY"


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def split_file_into_list(file):
    lines = file.split("\n")
    chracters_list = []
    for line in lines:
        temp_list = []
        for letter in line:
            temp_list.append(letter)
        chracters_list.append(temp_list)
    return chracters_list

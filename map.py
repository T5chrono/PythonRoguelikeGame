from enum import Enum
from random import randint

class TileType(Enum):
    GRASS = 1
    ROCK = 2
    WATER = 3
    TREE = 4
    WALL = 5
    GATE = 6

class Tile():

    def __init__(self):
        self.tile_type = TileType(randint(1,5))
        self.is_player = False
        if self.tile_type == TileType.WALL:
            self.is_passable = False
        else:
            self.is_passable = True

class Board():
    
    def __init__(self):
        self.width = 80
        self.height = 10
        self.tiles = []
        self.signs_to_print = {"GRASS": "+", "ROCK": " ", "WATER": " ", "TREE": " ", "WALL": "■", "GATE": "O"}
       

    def create_board(self):
        for tile in range(0, self.height):
            temp_list = []
            for tile in range(0, self.width):
                temp_list.append(Tile())
            self.tiles.append(temp_list)

    def print_board(self):
        x_border = "■"
        y_border = "|"
        print(x_border*(self.width+2))
        for row in self.tiles:
            row_to_print = y_border
            for tile in row:
                row_to_print += self.signs_to_print[tile.tile_type.name]
            row_to_print += y_border
            print(row_to_print)
        print(x_border*(self.width+2))


if __name__ == "__main__":
    board = Board() 
    board.create_board()
    board.print_board()


    



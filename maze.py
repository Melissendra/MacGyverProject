""" Creation of the maze structure in terminal mode"""

import constants as c
import characters, random
import end_game_exceptions as ex
from items import Item


class Maze:
    def __init__(self, path, symbols, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # opening of the file txt where is draw the maze
        with open(path) as f:
            self._maze_txt = [line.strip("\n") for line in f.readlines()]
        self.height = len(self._maze_txt)
        self.width = len(self._maze_txt[0])
        self._open_path = set()
        self._start = None
        self._arrival = None
        self.mac = None
        self.murdoc = None
        self.create_maze()
        self.add_items(symbols)

    def create_maze(self):
        """ iteration and creation of the maze while reading the file"""
        for y, line in enumerate(self._maze_txt):
            for x, char in enumerate(line.strip('\n')):
                if char in c.VALID_CHAR:
                    self._open_path.add((x, y))
                if char == 's':
                    self._start = {(x, y)}
                    self.mac = characters.Hero('👮‍♂️', list(self._start)[0], self)
                elif char == 'e':
                    self._arrival = {(x, y)}
                    self.murdoc = characters.Character('🧟‍♂️', list(self._arrival)[0], self)

    def draw(self):
        """ drawing of the maze"""
        mac_position = self.mac.x, self.mac.y
        for j in range(self.width):
            for i in range(self.height):
                if (i, j) == mac_position:
                    print(self.mac.char_rect, end='')
                elif (i, j) in self._arrival:
                    print(self.murdoc.char_rect, end='')
                elif (i, j) in self.items:
                    print(self.items[i, j].symbol, end='')
                elif (i, j) in self._open_path:
                    print('⬜', end='')
                else:
                    print('⬛', end='')
            print()

    def get_height(self):
        """ return the height of the maze """
        return self.height

    def get_width(self):
        """ We check if the maze has the same width everywhere
            and return the maze's width
        """
        maze_width = all(len(item) == self.width for item in self._maze_txt)
        if maze_width is False:
            print(" The maze's width is not the same in each line. ")
        return self.width

    def is_valid(self, position):
        """ check if it's not a wall """
        return position in self._open_path

    def is_arrival(self, position):
        """ check if the position is the arrival """
        return position in self._arrival

    def free_place(self):
        """check if there's not another item"""
        return self._open_path - self._start - self._arrival

    def add_items(self, symbols):
        """ addition randomly of items """
        available_symbols = symbols
        items_pos = random.sample(self.free_place(), 3)
        self.items = {}
        for pos, symbol in zip(items_pos, available_symbols):
            self.items[pos] = Item(pos, symbol)

    def has_object(self, position):
        """ check if the path contains an item"""
        return position in self.items

    def remove_item(self, position):
        """remove the item of the path when Mac takes it"""
        del self.items[position]


if __name__ == '__main__':
    """ How we launch the game """
    symbols = ['💉', '🧪', '💎']
    maze = Maze("maze_draw1.txt", symbols)
    mac = maze.mac

    try:
        while True:
            maze.draw()
            answer = input("What direction do you want to take ?")
            if answer in ['up', 'right', 'down', 'left']:
                mac.move(answer)
            elif answer == 'q':
                break

    except ex.HasLostGame as e:
        print(e)
    except ex.HasWonGame as e :
        print(e)



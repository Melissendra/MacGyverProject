import constants as c
import Characters
""" Creation of the maze structure """


class Maze(object):

    def __init__(self, path):
        with open(path) as f:
            self._maze_txt = [line.strip("\n") for line in f.readlines()]
        self.height = len(self._maze_txt)
        self.width = len(self._maze_txt[0])
        self._open_path = set()
        self._start = None
        self._arrival = None
        self.mac = Characters()
        self.mac_pos = self.start
    def create_maze(self):
        for y, line in enumerate(self._maze_txt):
            for x, char in enumerate(line.strip('\n')):
                if char in c.VALID_CHAR:
                    self._open_path.add((x, y))
                if char == 's':
                    self._start = (x, y)
                elif char == 'e':
                    self._arrival = (x, y)

    def draw_maze(self):
        self.create_maze()
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == self._start:
                    print('s', end='')
                elif (i, j) == self._arrival:
                    print('e', end='')
                elif (i, j) in self._open_path:
                    print('.', end='')
                else:
                    print('m', end='')
            print()

    def get_height(self):
        return self.height

    """ We check if the maze has the same width everywhere """
    def get_width(self):
        maze_width = all(len(item) == self.width for item in self._maze_txt)
        if maze_width is False:
            print(" The maze's width is not the same in each line. ")
        return self.width

    def is_valid(self, position):
        return position in self._open_path

    def is_arrival(self, position):
        return position in self._arrival


if __name__ == '__main__':
    maze = Maze("maze_draw1.txt")
    maze.draw_maze()

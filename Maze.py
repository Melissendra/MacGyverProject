import constants as c

""" Creation of the maze structure """


class Maze(object):

    def __init__(self, path):
        with open(path) as f:
            self.maze_txt = [line.strip("\n") for line in f.readlines()]
        self.get_height()
        self.get_width()


    def create_maze(self):
        
        open_path = []
        for y, line in enumerate(self.maze_txt):
             for x, char in enumerate(line.strip('\n')):
                if char in c.VALID_CHAR:
                    open_path.append((x, y))
    
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in open_path:
                    print('.', end='')
                else:
                    print('m', end='')
            print()

    def get_height(self):
        self.height = len(self.maze_txt)
        return self.height

    def get_width(self):
        self.width = len(self.maze_txt[0])
        maze_width = all(len(item) == self.width for item in self.maze_txt)
        if  maze_width is False:
            print(" The maze's width is not the same in each line. ")
        return self.width



if __name__ == '__main__':
    maze = Maze("maze_draw1.txt")
    maze.create_maze()

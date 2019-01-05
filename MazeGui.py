import Maze
import pygame
import CharactersGUI as chg
import constants as c


"""Graphic version of the maze"""


class MazeGui(Maze, pygame.sprite.Sprite):
    def __init__(self, *args, **kargs):
        pygame.init()
        super().__init__(*args, **kargs)
        
    def create_maze(self):
        for y, line in enumerate(self._maze_text):
            for x, char in enumerate(line.strip('\n')):
                if char in c.VALID_CHAR:
                    self._open_path.add((x, y))
                if char == 's':
                    self._start = (x, y)
                    self.mac = chg(self.char_right, self._start, self)
                elif char == 'e':
                    self._arrival = (x, y)
                    self.murdoc = chg(c.MURDOC_IMG, self._arrival, self)

    # def draw(self):
    #     self.window = pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE))
    #     mac_position = self.mac.x, self.mac.y
    #     for j in range(self.height):
    #         for i in range(self.width):
    #             if (i, j) == mac_position:
    #                 pygame.image.load()
    #             elif (i, j) == self._arrival:
    #                 print(self.murdoc.char_rect, end='')
    #             elif (i, j) in self.items:
    #                 print(self.items[i, j].symbol, end='')
    #             elif (i, j) in self._open_path:
    #                 print('⬜', end='')
    #             else:
    #                 print('⬛', end='')
    #         print()



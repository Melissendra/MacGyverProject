from CharactersGui import HeroGUI, GuardianGUI
import pygame
import constants as c
from pygame.locals import KEYDOWN, K_UP, K_DOWN, K_RIGHT, K_LEFT, K_ESCAPE, QUIT 
from Maze import Maze


""" Creation of the Maze's interface graphic with pygame"""


class MazeGui(Maze):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wall_img = pygame.image.load(c.WALL_IMG).convert()
        self.floor_img = pygame.image.load(c.FLOOR_IMG).convert()
        self.screen = pygame.display.get_surface()
        self.mac = HeroGUI('h', list(self._start)[0], self)
        self.murdoc = GuardianGUI('g', list(self._arrival)[0], self)
    
    def draw(self):
        mac_position = self.mac.x, self.mac.y
        murdoc_position = self.murdoc.x, self.murdoc.y
        for j in range(self.height):
            for i in range(self.width):
                if (i, j) in self._open_path:
                    self.screen.blit(self.floor_img, (i * c.SPRITE_SIZE, j * c.SPRITE_SIZE))
                else:
                    self.screen.blit(self.wall_img, (i * c.SPRITE_SIZE, j * c.SPRITE_SIZE))

                if (i, j) == mac_position:
                    self.screen.blit(self.mac.image, self.mac.rect)
                elif (i, j) == murdoc_position:
                    self.screen.blit(self.murdoc.image, self.murdoc.rect)
                elif (i, j) in self.items:
                    self.screen.blit(self.items[i, j].symbol, (i * c.SPRITE_SIZE, j * c.SPRITE_SIZE))



if __name__ == '__main__':
    pygame.init()
    pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE))
    
    symbols = [
        pygame.image.load(c.NEEDLE_IMG).convert_alpha(), 
        pygame.image.load(c.SYRINGE).convert_alpha(),
        pygame.image.load(c.ETHER_IMG).convert_alpha()
    ]

    maze = MazeGui("maze_draw1.txt", symbols)
    mac = maze.mac
    running = True
    while running:
        maze.draw()
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
        
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    mac.move("right")
                elif  event.key == K_LEFT:
                    mac.move("left")
                elif  event.key == K_DOWN:
                    mac.move("down")
                elif event.key == K_UP:
                    mac.move("up")

        maze.screen.blit(mac.image, mac.rect)
        pygame.display.flip()

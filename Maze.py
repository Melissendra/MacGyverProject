import pygame

from pygame.locals import *

from constants import *
from MacGyver import *


"""Creation of the maze"""
class Maze():

    def __init__(self, window='default'):
        self.window = window
        pygame.init()

    def home_page(self):
        window = pygame.display.set_mode((window_size, window_size))

        # Window's icon
        icon = pygame.image.load(window_icone)
        pygame.display.set_icon(icon)

        # Title
        pygame.display.set_caption(window_title)

        # opening of the home page
        pygame.time.Clock().tick(30)
        home = pygame.image.load(home_page).convert()
        window.blit(home, (0, 0))

        # Welcome sentence
        font = pygame.font.Font(None, 35)
        welcome_text = font.render ("Welcome to MacGyver's Maze !", 0, (58, 252, 139))
        window.blit(welcome_text, (30, 70))

        pygame.display.flip()

    # principal loop
    def run(self):
        # Window initialization
        self.home_page()
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False

        

if __name__ == '__main__':
    Maze().run()





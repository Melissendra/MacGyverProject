import pygame

from pygame.locals import *
from sys import exit
from constants import *
from MacGyver import *


"""Creation of the maze"""
class Maze():
    # Window initialization
    def __init__(self, window):
        self.window = window
        pygame.init()

        # Opening window's Maze Game
        window = pygame.display.set_mode((window_size, window_size))

        # Window's icon
        icon = pygame.image.load(window_icone)
        pygame.display.set_icon(icon)

        # Title
        pygame.display.set_caption(window_title)


    # principal loop
    def game():
        gaming =True
        while gaming:
            # Opening of the Home's page
            home = pygame.image.load(home_page).convert()
            window.blit(home, (0, 0))

            # refresh
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    gaming = False
                    exit()


#     carry_on_game = True
#     carry_on_home =True

#     # Welcome loop
#     while carry_on_home:
#         pygame.time.Clock().tick(30)

#         sys_font = pygame.font.SysFont("Arial", 24)
#         welcome_text = sys_font.render("Welcome to MacGyver's Maze Game !", 0, (58,252,139))
#         window.blit(welcome_text, (15,70))

#         for event in pygame.event.get():
#             # For leaving the game
#             if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
#                pygame.quit()
#                sys.exit()
#                # Play variable
#                play = 0

            
#             elif event.type == KEYDOWN:
#                 if event.key == K_RETURN:
#                     carry_on_home = False
#                     play = "maze_draw1.txt"

        
#         pygame.display.flip()
                
               




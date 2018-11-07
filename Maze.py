import pygame
from pygame.locals import *

from constants import *
from MacGyver import *



"""Creation of the maze"""

pygame.init()

# Opening window's Maze Game
window = pygame.display.set_mode((window_size, window_size))

# Window's icon
icon = pygame.image.load(window_icone)
pygame.display.set_icon(icon)

# Title
pygame.display.set_caption(window_title)


# principal loop
carry_on = 1
while carry_on:
    # Opening of the Home's page
    home = pygame.image.load(home_page).convert()
    window.blit(home, (0, 0))

    # refresh
    pygame.display.flip()

    carry_on_game = 1
    carry_on_home =1




import pygame
from pygame.locals import *
from constants import *

""" creation of MacGyver perso, whho is the only personnage to move in the maze"""


class MacGyver():
    def __init__(self, maze):
        # MacGyver's sprite
        self.img = pygame.image.load(macGyver_img).convert_alpha()
        # Where MacGyver is
        self.maze = maze
        # MacGyver's position in case and pixel
        self.case_x = 6
        self.case_y = 0
        self.x = 192
        self.y = 0  

    def motions(self, direction):
        #motion to the right
        if direction == "right":
            # for not trespassing the screen
            if self.case_x < (sprite_nb - 1):
                # we look that Macgyver does'nt go in a wall
                if self.maze_structure[self.case_y][self.case_x + 1] != "m":
                    # motion of one case
                    self.case_x += 1
                    # calculation of the position in px
                    self.x = self.case_x * sprite_size

        # motion to the left
        if direction == "left":
            if self.case_x > 0 :
                if self.maze_structure[self.case_y][self.case_x - 1] != "m":
                    self.case_x -= 1 
                    self.x = self.case_x * sprite_size
        
        # motion to the top
        if direction == "top":
            if self.case_y > 0:
                if self.maze_structure[self.case_y - 1][self.case_x] != "m":
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size




    
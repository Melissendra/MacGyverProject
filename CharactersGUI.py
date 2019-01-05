import pygame
from Characters import Hero
import constants as c
from pygame.locals import *

""" Graphic version of Characters class with sprites """


class CharactersGUI(Hero, pygame.Sprite):
    def __init__(self, char_rec, position, maze, *args, **kargs):
        super().__init__(*args, **kargs)
        self.char_left = pygame.image.load(c.MACGYVER_LEFT).convert_alpha()
        self.char_right = pygame.image.load(c.MACGYVER_RIGHT).convert_alpha()
        self.char_up = pygame.image.load(c.MACGYVER_UP).convert_alpha()
        self.char_down = pygame.image.load(c.MACGYVER_DOWN).convert_alpha()

        # the speed deplacement is calculated in SPRITE_SIZE
        self.speed = c.SPRITE_SIZE
    
    def move(self, direction):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    x, y = self.x, self.y - self.speed
                elif event.key == K_DOWN:
                    x, y = self.x, self.y + self.speed
                elif event.key == K_LEFT:
                    x, y = self.x - self.speed, self.y
                elif event.key == K_RIGHT:
                    x, y = self.x + self.speed, self.y


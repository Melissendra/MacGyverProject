import pygame, os
from Characters import Hero, Character
import constants as c
from pygame.locals import *


""" Graphic version of Characters class with sprites """

data_dir = os.path.join(os.path.dirname(__file__))


# functions to create our resources


def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    img = pygame.image.load(fullname)
    img = img.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = img.get_at((0,0))
        img.set_colorkey(colorkey, RLEACCEL)
    return img, img.get_rect()


class HeroGUI(Hero):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.char_left_img = load_image(c.MACGYVER_LEFT, -1)
        self.char_right_img = load_image(c.MACGYVER_RIGHT, -1)
        self.char_up_img = load_image(c.MACGYVER_UP, -1)
        self.char_down_img = load_image(c.MACGYVER_DOWN, -1)
        self.image, self.rect =  self.char_right_img
        self.rect.topleft = (0,0)

    def move(self, direction):
        super().move(direction)
        if direction == "up":
            self.image = self.char_up_img
        elif direction == "down":
            self.image = self.char_down_img
        elif direction == "right":
            self.image = self.char_right_img
        elif direction == "left":
            self.image = self.char_left_img


class GuardianGUI(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image, self.rect  = load_image(c.MURDOCH_IMG, -1)
        self.rect.topleft = (self.x * c.SPRITE_SIZE, self.y * c.SPRITE_SIZE)

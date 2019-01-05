import pygame
from Items import Item
import constants as c
from enum import Enum


""" Items graphique version """


class Symbols(Enum):
    NEEDLE = pygame.image.load(c.NEEDLE_IMG)
    SYRINGE = pygame.image.load(c.SYRINGE)
    NEEDLE = pygame.image.load(c.NEEDLE_IMG)


class ItemGui(Item, pygame.Sprite):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)


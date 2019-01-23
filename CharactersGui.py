import pygame
from Characters import Hero, Character
import constants as c


class HeroGUI(Hero):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.char_left_img = pygame.image.load(c.MACGYVER_LEFT).convert_alpha()
        self.char_right_img = pygame.image.load(c.MACGYVER_RIGHT).convert_alpha()
        self.char_up_img = pygame.image.load(c.MACGYVER_UP).convert_alpha()
        self.char_down_img = pygame.image.load(c.MACGYVER_DOWN).convert_alpha()
        self.image = self.char_right_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

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

        self.rect.topleft = (self.x * c.SPRITE_SIZE, self.y * c.SPRITE_SIZE)


class GuardianGUI(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = pygame.image.load(c.MURDOCH_IMG).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * c.SPRITE_SIZE, self.y * c.SPRITE_SIZE)

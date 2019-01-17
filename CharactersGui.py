import pygame
from Characters import Hero, Character
import Exceptions as ex
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

        if  direction == "up":
            self.image = self.char_up_img
        elif direction == "down":
            self.image = self.char_down_img
        elif direction == "right":
            self.image = self.char_right_img
        elif direction == "left":
            self.image = self.char_left_img

        self.rect.topleft = (self.x * c.SPRITE_SIZE, self.y * c.SPRITE_SIZE)

    # def is_finished(self):
    #     super().is_finished()
    #     self.pop_up = pygame.display.set_mode((100 , 80))
    #     font = pygame.font.Font("resources/Arcon-Regular.otf", 25)
    #     winning_txt = font.render("You win!!!", 0, c.DARKER_GREEN)
    #     pos_winning_txt = winning_txt.get_rect().center
    #     if self.maze.is_arrival:
    #         if len(self.inventory) == c.ITEMS_NUMBER:
    #             try:
    #                 raise ex.HasWonGame()
    #             except:

    #             self.pop_up.blit(winning_txt, pos_winning_txt)

    #         else:
    #             raise ex.HasLostGame("You're dead !!!")


class GuardianGUI(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = pygame.image.load(c.MURDOCH_IMG).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * c.SPRITE_SIZE, self.y * c.SPRITE_SIZE)

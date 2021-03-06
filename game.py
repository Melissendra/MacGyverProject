"""Creation of the Home Page"""


import pygame
import buttons
import mazeGUI
import constants as c
from pygame.locals import K_ESCAPE, QUIT, KEYDOWN


class Game:
    def __init__(self):
        pygame.init()
        self.home_page()

    def home_page(self):
        """ Welcome Page creation which contain a
            welcoming sentence and button to attain
            the game.
        """
        self.window = pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE))
        rect = self.window.get_rect()

        """ Window's icon """
        icon = pygame.image.load(c.WINDOW_ICON)
        pygame.display.set_icon(icon)

        """ Title """
        pygame.display.set_caption(c.WINDOW_TITLE)

        """ opening of the home page """
        pygame.time.Clock().tick(30)
        home = pygame.image.load(c.HOME_PAGE).convert()
        self.window.blit(home, (0, 0))

        """ Welcome sentence """
        font = pygame.font.Font("resources/Arcon-Regular.otf", 40)
        welcome_text = font.render("Welcome to MacGyver's Maze !", 0, c.DARKER_GREEN)
        pos_welcome_txt = welcome_text.get_rect()
        pos_welcome_txt.center = self.window.get_rect().center
        pos_welcome_txt.y -= 330
        self.window.blit(welcome_text, pos_welcome_txt)
        self.play_b = buttons.ClickableButton((rect.centerx, rect.centery + 300), (100, 40), c.LIGHT_GREEN, "Play", "Play")

    def run(self):
        """ The welcome loop """
        running_welcome = True
        while running_welcome:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        exit()
                if event.type == pygame.mouse.get_pressed():
                    running_welcome = False
                    mazeGUI.main()

            self.play_b.update(self.window)
            pygame.display.flip()


if __name__ == '__main__':
    play_game = Game()
    play_game.run()

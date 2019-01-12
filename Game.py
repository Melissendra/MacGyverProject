import pygame

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
import constants as c
from Buttons import PlayButton


"""Creation of the maze"""


class Game():

    def __init__(self):
        pygame.init()

    """  Welcome Page creation which contain a welcoming sentence and button to attain the game."""
    def home_page(self):
        self.window = pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE))
        rect = self.window.get_rect()
        
        play_b = PlayButton((rect.centerx, rect.centery + 330), (100, 40), c.LIGHT_GREEN, "Play")

        # Window's icon
        icon = pygame.image.load(c.WINDOW_ICON)
        pygame.display.set_icon(icon)

        # Title
        pygame.display.set_caption(c.WINDOW_TITLE)

        # opening of the home page
        pygame.time.Clock().tick(30)
        home = pygame.image.load(c.HOME_PAGE).convert()
        self.window.blit(home, (0, 0))

        # Welcome sentence
        font = pygame.font.Font("resources/Arcon-Regular.otf", 30)
        welcome_text = font.render("Welcome to MacGyver's Maze !", 0, c.DARKER_GREEN)
        pos_welcome_txt = welcome_text.get_rect()
        pos_welcome_txt.center = self.window.get_rect().center
        pos_welcome_txt.y -= 330
        self.window.blit(welcome_text, pos_welcome_txt)

        play_b.update(self.window)

        pygame.display.flip()

    """ The principal loop """
    def run(self):

        running = True
        while running:
            print(pygame.mouse.get_pressed())

            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False

            # Window initialization
            self.home_page()

            pygame.display.flip()


if __name__ == '__main__':
    Game().run()





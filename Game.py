import pygame

from pygame.locals import *
from constants import *
from Buttons import PlayButton


"""Creation of the maze"""


class Game:

    def __init__(self):
        pygame.init()

    def home_page(self):
        self.window = pygame.display.set_mode((window_size, window_size))
        rect = self.window.get_rect()
        
        play_b = PlayButton((rect.centerx, rect.centery + 210), (100, 40), light_green, "Play")

        # Window's icon
        icon = pygame.image.load(window_icon)
        pygame.display.set_icon(icon)

        # Title
        pygame.display.set_caption(window_title)

        # opening of the home page
        pygame.time.Clock().tick(30)
        home = pygame.image.load(home_page).convert()
        self.window.blit(home, (0, 0))

        # Welcome sentence
        font = pygame.font.Font("resources/Arcon-Regular.otf", 30)
        welcome_text = font.render("Welcome to MacGyver's Maze !", 0,light_green)
        pos_welcome_txt = welcome_text.get_rect()
        pos_welcome_txt.center = self.window.get_rect().center
        pos_welcome_txt.y -= 200
        self.window.blit(welcome_text, pos_welcome_txt)

        play_b.update(self.window)

        pygame.display.flip()

    # principal loop
    def run(self):
        # Window initialization
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False
        
            self.home_page()

            pygame.display.flip()


if __name__ == '__main__':
    Game().run()





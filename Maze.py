import pygame

# -tc- de manière générale, éviter les imports de ce type
from pygame.locals import *

from constants import *



"""Creation of the maze"""

# -tc- ajouter des docstrings à chaque module, classe, méthode, fonction
class Maze:

    def __init__(self):
        pygame.init()

    def home_page(self):
        self.window = pygame.display.set_mode((window_size, window_size))

        # Window's icon
        icon = pygame.image.load(window_icon)
        pygame.display.set_icon(icon)

        # Title
        pygame.display.set_caption(window_title)

        # opening of the home page
        pygame.time.Clock().tick(30)
        home = pygame.image.load(home_page).convert()
        self.window.blit(home, (0, 0))
        self.play_button()

        # Welcome sentence
        font = pygame.font.Font("resources/Arcon-Regular.otf", 30)
        welcome_text = font.render("Welcome to MacGyver's Maze !", 0, (58, 252, 139))
        self.window.blit(welcome_text, (35, 20))

        pygame.display.flip()

    # -tc- éventuellement, le bouton peut être une classe à part
    def play_button(self):
        # -tc- D'où vient before_clicked? C'est pour cela qu'il faut éviter: les from module import *
        play_b = pygame.draw.rect(self.window, before_clicked, [190, 430, 100, 40], 5)
        # pos_play_b = 190, 430
        # play_b.fill(before_clicked)
        font_button = pygame.font.Font('resources/Arcon-Regular.otf', 22)
        button_text = font_button.render("Play", 1, (0, 0, 0))
        pos_button_txt = 222, 435

        # Mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Is the mouse in the button
        over_play_b = play_b.collidepoint(mouse_pos)
        # self.window.blit(play_b, pos_play_b)
        self.window.blit(button_text, pos_button_txt)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if over_play_b:
                    before_clicked = after_clicked

    # principal loop
    def run(self):
        # Window initialization
        self.home_page()
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False

    
if __name__ == '__main__':
    Maze().run()





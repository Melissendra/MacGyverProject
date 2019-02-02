""" Creation of the Maze's interface graphic with pygame """


import pygame
import buttons
import constants as c
import end_game_exceptions as ex
from charactersGui import HeroGUI, GuardianGUI
from pygame.locals import KEYDOWN, K_UP, K_DOWN, K_RIGHT, K_LEFT, K_ESCAPE, QUIT
from maze import Maze


class MazeGui(Maze):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wall_img = pygame.image.load(c.WALL_IMG).convert()
        self.floor_img = pygame.image.load(c.FLOOR_IMG).convert()
        self.screen = pygame.display.get_surface()
        self.mac = HeroGUI('h', list(self._start)[0], self)
        self.murdoc = GuardianGUI('g', list(self._arrival)[0], self)
        self.mac_position = self.mac.x, self.mac.y
        self.murdoc_position = self.murdoc.x, self.murdoc.y

    def draw(self):
        """ we draw the maze with an interface and sprites """
        for i in range(self.width):
            for j in range(self.height):
                if (i, j) in self._open_path:
                    self.screen.blit(self.floor_img, (i * c.SPRITE_SIZE, j * c.SPRITE_SIZE))
                else:
                    self.screen.blit(self.wall_img, (i * c.SPRITE_SIZE, j * c.SPRITE_SIZE))

                if (i, j) == self.mac_position:
                    self.screen.blit(self.mac.image, self.mac.rect)
                elif (i, j) == self.murdoc_position:
                    self.screen.blit(self.murdoc.image, self.murdoc.rect)
                elif (i, j) in self.items:
                    self.screen.blit(self.items[i, j].symbol, (i * c.SPRITE_SIZE, j * c.SPRITE_SIZE))

    def remove_item(self, position):
        """ we define how we remove the items when Mac takes it """
        items_sound = load_sound(c.ITEMS_TAKEN)
        super().remove_item(position)
        items_sound.play()
        self.mac.item_taken += 1

    def scoring(self):
        """ Creation of a item's counter"""
        font = pygame.font.Font("resources/Arcon-Regular.otf", 25)
        items_txt = font.render("Items: " + str(self.mac.item_taken), True, c.BLACK)
        self.screen.blit(items_txt, (20, 760))

    def finished_window(self, text):
        """draw the window that pop when Mac arrive on the final case """
        game_finished = pygame.Surface((400, 200)).convert()
        game_finished.fill(c.WHITE)
        font = pygame.font.Font("resources/Arcon-Regular.otf", 25)
        finished_txt = font.render(text, 0, c.BLACK)
        finished_txt_rect = finished_txt.get_rect()
        finished_txt_rect.center = (game_finished.get_width() / 2, 50)
        pos_game_finished = game_finished.get_rect()
        pos_game_finished.center = (self.screen.get_width() / 2, self.screen.get_height() / 2)
        game_finished.blit(finished_txt, finished_txt_rect)
        self.screen.blit(game_finished, pos_game_finished)

        """ creation of the buttons display with its position and functions """
        play_b_pos = (pos_game_finished.left + 100, pos_game_finished.top + 150)
        quit_b_pos = (pos_game_finished.left + 300, pos_game_finished.top + 150)
        play_b = buttons.ClickableButton(play_b_pos, (120, 50), c.LIGHT_GREEN, "Play Again!", "Play")
        quit_b = buttons.ClickableButton(quit_b_pos, (120, 50), c.LIGHT_GREEN, "Quit!", "Quit")
        play_b.update(self.screen)
        quit_b.update(self.screen)


def load_sound(name):
    """we create a function to load sound """
    sound = pygame.mixer.Sound(name)
    return sound


def main():
    """ creation a function to launch the game """
    pygame.init()
    pygame.display.set_mode((c.WINDOW_SIZE, c.WINDOW_SIZE + 50))
    background = pygame.Surface((c.WINDOW_SIZE, c.WINDOW_SIZE+50))
    background.fill(c.WHITE)

    """ images of the items """
    symbols = [
        pygame.image.load(c.NEEDLE_IMG).convert_alpha(),
        pygame.image.load(c.SYRINGE).convert_alpha(),
        pygame.image.load(c.ETHER_IMG).convert_alpha()
        ]

    maze = MazeGui("maze_draw1.txt", symbols)
    mac = maze.mac
    victory_sound = load_sound(c.VICTORY_SOUND)
    rip_sound = load_sound(c.RIP_SOUND)
    running = True

    try:
        """ the main loop """
        while running:
            maze.screen.blit(background, (0, 0))
            maze.draw()
            maze.scoring()
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        mac.move("right")
                    elif event.key == K_LEFT:
                        mac.move("left")
                    elif event.key == K_DOWN:
                        mac.move("down")
                    elif event.key == K_UP:
                        mac.move("up")

            maze.screen.blit(mac.image, mac.rect)
            pygame.display.flip()

    except ex.HasWonGame:
        running = True
        victory_sound.play()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False
            maze.finished_window("You Win!!")
            pygame.display.flip()

    except ex.HasLostGame:
        running = True
        rip_sound.play()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False
            maze.finished_window("You're dead!!!")
            pygame.display.flip()

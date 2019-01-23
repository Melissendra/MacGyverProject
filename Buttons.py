import pygame

from pygame.locals import *
import constants as c


"""Creation of the Game's buttons"""

# Mother class


class ClickableButton:
    def __init__(self, pos, size):
        self.rect = pygame.Rect((0, 0), size)
        self.rect.center = pos
        self.has_clicked = False

    # détection if the mouse is over the button
    def is_mouse_over(self):

        # detect the posistion of the mouse
        cursor = pygame.mouse.get_pos()

        if self.rect.left < cursor[0] < self.rect.right and self.rect.top < cursor[1] < self.rect.bottom:
            return True
        else:
            return False

    def do_mouse_over(self):
        pass

    def is_left_mouse_down(self):
        if pygame.mouse.get_pressed()[0] == 1:
            return True
        else:
            return False

    def do_left_mouse_down(self):
        pass

    def is_clicked(self):
        # detect if the mouse button is pressed
        mouse = pygame.mouse.get_pressed()

        if mouse[0] == True and self.has_clicked == False and self.is_mouse_over():
            self.has_clicked = True
            return True
        if mouse[0] == False and self.has_clicked == True:
            self.has_clicked = False

        return False

    def do_click(self):
        pass

    def update(self, window):
        if self.is_mouse_over():
            self.do_mouse_over()

        if self.is_left_mouse_down():
            self.do_left_mouse_down()

        if self.is_clicked():
            self.do_click()


class PlayButton(ClickableButton):
    def __init__(self, pos, size, color, text):
        super().__init__(pos, size)

        self.color = color
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        self.font_button = pygame.font.Font("resources/Arcon-Regular.otf", 20)
        self.text = self.font_button.render(text, 0, c.BLACK)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.image.get_width() / 2, self.image.get_height() / 2)

    def do_mouse_over(self):
        over = pygame.Surface(self.rect.size)
        over.set_alpha(60)
        over.fill(c.BLACK)
        self.image.blit(over, (0, 0))

    def do_left_mouse_down(self):
        self.image.fill(c.RED)

    def do_click(self):
        print("You clicked a button")

    def draw(self, window):
        self.image.blit(self.text, self.text_rect)
        window.blit(self.image, self.rect)

    def update(self, window):
        self.image.fill(self.color)

        super().update(window)

        self.draw(window)


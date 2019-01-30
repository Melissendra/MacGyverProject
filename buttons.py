import pygame
import constants as c
import mazeGUI

"""Creation of the Game's buttons display and actions"""


class ClickableButton:
    def __init__(self, pos, size, color, text, action):
        self.rect = pygame.Rect((0, 0), size)
        self.rect.center = pos
        self.has_clicked = False
        self.color = color
        self.action = action
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        self.font_button = pygame.font.Font("resources/Arcon-Regular.otf", 20)
        self.text = self.font_button.render(text, 0, c.BLACK)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.image.get_width() / 2, self.image.get_height() / 2)

    # detection if the mouse is over the button
    def is_mouse_over(self):
        # detect the position of the mouse
        cursor = pygame.mouse.get_pos()
        if self.rect.left < cursor[0] < self.rect.right and self.rect.top < cursor[1] < self.rect.bottom:
            return True
        else:
            return False

    # colors the buttons when the mouse is over the button
    def do_mouse_over(self):
        over = pygame.Surface(self.rect.size)
        over.set_alpha(60)
        over.fill(c.BLACK)
        self.image.blit(over, (0, 0))

    # detection of the mouse's pressed
    def is_left_mouse_down(self):
        if self.is_mouse_over() and pygame.mouse.get_pressed()[0] == 1:         # click left
            return True
        else:
            return False

    def do_left_mouse_down(self):
        self.image.fill(c.RED)

    def is_clicked(self):
        # detect if the mouse button is pressed
        mouse = pygame.mouse.get_pressed()
        if mouse[0] is True and self.has_clicked is False and self.is_mouse_over():
            self.has_clicked = True
            return True
        if mouse[0] is False and self.has_clicked is True:
            self.has_clicked = False

        return False

    def do_click(self):
        if self.action == "Play":
            mazeGUI.main()
        if self.action == "Quit":
            exit()

    # draw the button on the window
    def draw(self, window):
        self.image.blit(self.text, self.text_rect)
        window.blit(self.image, self.rect)

    # check the state of the mouse and update it
    def update(self, window):
        if self.is_mouse_over():
            self.do_mouse_over()

        if self.is_left_mouse_down():
            self.do_left_mouse_down()

        if self.is_clicked():
            self.do_click()

        self.image.fill(self.color)
        self.draw(window)


import pygame


""" Here we create the characters of the game with their moves and position. """


class Character:
    def __init__(self, position, maze):
        #self.char_left = pygame.image.load(left).convert_alpha()
        #self.char_right = pygame.image.load(right).convert_alpha()
        #self.char_up = pygame.image.load(up).convert_alpha()
        #self.char_down = pygame.image.load(down).convert_alpha()
        #self.character_rect = self.char_right.get_rect()

        # speed of MacGyver's deplacements
        self.speed = 1
        self.position = position

        # Maze instance
        self.maze = maze

    def move_char(self, direction):
        direction = input(" Which direction would you want to take? ")
        if direction == "up" and self.maze.is_valid():
            self.character_rect.y -= self.speed
        if direction == "down" and self.maze.is_valid():
            self.character_rect.y += self.speed
        if direction == "left" and self.maze.is_valid():
            self.character_rect.x += self.speed
        if direction == "right" and self.maze.is_valid():
            self.character_rect.x -= self.speed

    def set_character_rect(self, x, y):
        self.character_rect.x = x
        self.character_rect.y = y

    def get_character_rect(self):
        return self.character_rect


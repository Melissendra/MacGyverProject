import pygame
import Maze

""" Here we create the characters of the game with their moves and position. """


class Character:
    def __init__(self,char_rect, position, maze):
        #self.char_left = pygame.image.load(left).convert_alpha()
        #self.char_right = pygame.image.load(right).convert_alpha()
        #self.char_up = pygame.image.load(up).convert_alpha()
        #self.char_down = pygame.image.load(down).convert_alpha()
        #self.character_rect = self.char_right.get_rect()
        self.char_rect = char_rect
        
        # speed of MacGyver's deplacements
        self.x, self.y = position

        # Maze instance
        self.maze = maze

class Hero(Character):
    def __init__(self,char_rect, position, maze):
        super().__init__(char_rect, position, maze)
        self.speed = 1

    def move(self, direction):
        if direction == "up":
            x, y = self.x, self.y - 1
                
        elif direction == "down":
            x, y = self.x, self.y + 1
            
        elif direction == "left":
            x, y = self.x - 1, self.y
        
        elif direction == "right":
            x, y = self.x + 1, self.y

        if self.maze.is_valid((x, y)):
            self.x, self.y = x, y


    



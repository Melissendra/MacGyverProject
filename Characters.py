import pygame
import Maze
import constants as c
""" Here we create the characters of the game with their moves and position. """


class Character:
    def __init__(self, char_rect, position, maze):
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
    def __init__(self, char_rect, position, maze):
        super().__init__(char_rect, position, maze)
        self.speed = 1
        self.inventory = []
        

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
        
        if self.maze.has_object((x, y)):
            item = self.maze.items[x, y]
            self.inventory.append(item)
            self.maze.remove_item((x,y))
            print(self.inventory)
           
    def has_win(self):
        if len(self.inventory) == c.ITEMS_NUMBER:
            print("You win !!")

   
        


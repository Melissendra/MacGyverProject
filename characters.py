"""
    Here we create the characters of the game with their moves and position.
    In terminal mode
"""

from maze import Maze
import constants as c
import end_game_exceptions as ex


class Character:
    def __init__(self, char_rect, position, maze, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.char_rect = char_rect
        self.x, self.y = position
        self.maze = maze


class Hero(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = 1
        self.inventory = []
        self.item_taken = 0

    def move(self, direction):
        """
            define how the character moves
        """
        if direction == "up":
            x, y = self.x, self.y - self.speed

        elif direction == "down":
            x, y = self.x, self.y + self.speed

        elif direction == "left":
            x, y = self.x - self.speed, self.y

        elif direction == "right":
            x, y = self.x + self.speed, self.y

        if self.maze.is_valid((x, y)):
            """ check if it's a path and not a wall
                and allow the hero
            """
            self.x, self.y = x, y

        if self.maze.has_object((x, y)):
            """ check if there is an item in the new
                Mac's position
            """
            item = self.maze.items[x, y]
            self.inventory.append(item)
            self.maze.remove_item((x, y))
            print("Items:" + str(self.item_taken))

        if self.maze.is_arrival((x, y)):
            self.is_finished()

    def is_finished(self):
        """ check if the inventory contains the 3 needed items
            and tell if Mac Win or die
        """
        if self.maze.is_arrival:
            if len(self.inventory) == c.ITEMS_NUMBER:
                raise ex.HasWonGame("You win !!!")
            else:
                raise ex.HasLostGame("You're dead !!!")

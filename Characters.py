import Maze
import constants as c
import Exceptions as ex

""" Here we create the characters of the game with their moves and position. """


class Character:
    def __init__(self, char_rect, position, maze, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.char_rect = char_rect
        self.x, self.y = position
        # Maze instance
        self.maze = maze
        self.speed = 1


class Hero(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = 1
        self.inventory = []

    def move(self, direction):
        if direction == "up":
            x, y = self.x, self.y - self.speed

        elif direction == "down":
            x, y = self.x, self.y + self.speed

        elif direction == "left":
            x, y = self.x - self.speed, self.y

        elif direction == "right":
            x, y = self.x + self.speed, self.y

        if self.maze.is_valid((x, y)):
            self.x, self.y = x, y
        
        if self.maze.has_object((x, y)):
            item = self.maze.items[x, y]
            self.inventory.append(item)
            self.maze.remove_item((x,y))
            print(self.inventory)

        if self.maze.is_arrival((x, y)):
            self.is_finished()

    def is_finished(self):
        if self.maze.is_arrival:
            if len(self.inventory) == c.ITEMS_NUMBER:
                raise ex.HasWonGame("You win !!!")
            else:
                raise ex.HasLostGame("You're dead !!!")


class Guardian(Character):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

import random
from enum import Enum

"""We create the items which'll be positionned randomly in the maze"""


class Symbols(Enum):
    NEEDLE = 'N'
    SYRINGE = 'P'
    ETHER = 'T'


class Item:
    def __init__(self, position, symbol):
        self.x, self.y = position
        self.symbol = symbol.value










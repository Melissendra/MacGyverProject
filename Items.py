from enum import Enum

"""We create the items which'll be positionned randomly in the maze"""


class Symbols(Enum):
    NEEDLE = '🗡️ '
    SYRINGE = '📏'
    ETHER = '💧'


class Item:
    def __init__(self, position, symbol, *args, **kargs):
        super().__init__(*args, **kargs)
        self.x, self.y = position
        self.symbol = symbol.value










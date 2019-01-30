
"""We create the items which will be positioned randomly in the maze"""


class Item:
    def __init__(self, position, symbol, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x, self.y = position
        self.symbol = symbol










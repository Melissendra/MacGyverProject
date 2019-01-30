"""We create our own exceptions to end the game"""


class HasWonGame(Exception):
    pass


class HasLostGame(Exception):
    pass


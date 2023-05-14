"""
    This module contains all tetrominoes and
    all his rotation state
"""

from pygame.math import Vector2
from tetromino import Block

class LBlock(Block):
    """The tetromino L shape"""

    def __init__(self):
        super().__init__(id=1)
        self.cells = {
            0: [Vector2(0, 2), Vector2(1, 0), Vector2(1, 1), Vector2(1, 2)],
            1: [Vector2(0, 1), Vector2(1, 1), Vector2(2, 1), Vector2(2, 2)],
            2: [Vector2(1, 0), Vector2(1, 1), Vector2(1, 2), Vector2(2, 0)],
            3: [Vector2(0, 0), Vector2(0, 1), Vector2(1, 1), Vector2(2, 1)]
        }
        self.move(0, 3)


class IBlock(Block):
    """The tetromino I shape"""

    def __init__(self):
        super().__init__(id=2)
        self.cells = {
            0: [Vector2(1, 0), Vector2(1, 1), Vector2(1, 2), Vector2(1, 3)],
            1: [Vector2(0, 2), Vector2(1, 2), Vector2(2, 2), Vector2(3, 2)],
            2: [Vector2(2, 0), Vector2(2, 1), Vector2(2, 2), Vector2(2, 3)],
            3: [Vector2(0, 1), Vector2(1, 1), Vector2(2, 1), Vector2(3, 1)]
        }
        self.move(-1, 3)


class OBlock(Block):
    """The tetromino O shape"""

    def __init__(self):
        super().__init__(id=3)
        self.cells = {
            0: [Vector2(0, 0), Vector2(0, 1), Vector2(1, 0), Vector2(1, 1)],
            1: [Vector2(0, 0), Vector2(0, 1), Vector2(1, 0), Vector2(1, 1)],
            2: [Vector2(0, 0), Vector2(0, 1), Vector2(1, 0), Vector2(1, 1)],
            3: [Vector2(0, 0), Vector2(0, 1), Vector2(1, 0), Vector2(1, 1)]
        }
        self.move(0, 4)


class SBlock(Block):
    """The tetromino S shape"""

    def __init__(self):
        super().__init__(id=4)
        self.cells = {
            0: [Vector2(0, 1), Vector2(0, 2), Vector2(1, 0), Vector2(1, 1)],
            1: [Vector2(0, 1), Vector2(1, 1), Vector2(1, 2), Vector2(2, 2)],
            2: [Vector2(1, 1), Vector2(1, 2), Vector2(2, 0), Vector2(2, 1)],
            3: [Vector2(0, 0), Vector2(1, 0), Vector2(1, 1), Vector2(2, 1)]
        }
        self.move(0, 3)


class TBlock(Block):
    """The tetromino T shape"""

    def __init__(self):
        super().__init__(id=5)
        self.cells = {
            0: [Vector2(0, 1), Vector2(1, 0), Vector2(1, 1), Vector2(1, 2)],
            1: [Vector2(0, 1), Vector2(1, 1), Vector2(1, 2), Vector2(2, 1)],
            2: [Vector2(1, 0), Vector2(1, 1), Vector2(1, 2), Vector2(2, 1)],
            3: [Vector2(0, 1), Vector2(1, 0), Vector2(1, 1), Vector2(2, 1)]
        }
        self.move(0, 3)


class ZBlock(Block):
    """The tetromino Z shape"""

    def __init__(self):
        super().__init__(id=6)
        self.cells = {
            0: [Vector2(0, 0), Vector2(0, 1), Vector2(1, 1), Vector2(1, 2)],
            1: [Vector2(0, 2), Vector2(1, 1), Vector2(1, 2), Vector2(2, 1)],
            2: [Vector2(1, 0), Vector2(1, 1), Vector2(2, 1), Vector2(2, 2)],
            3: [Vector2(0, 1), Vector2(1, 0), Vector2(1, 1), Vector2(2, 0)]
        }
        self.move(0, 3)


class JBlock(Block):
    """The tetromino J shape"""

    def __init__(self):
        super().__init__(id=7)
        self.cells = {
            0: [Vector2(0, 0), Vector2(0, 1), Vector2(0, 2), Vector2(1, 2)],
            1: [Vector2(0, 1), Vector2(1, 1), Vector2(2, 0), Vector2(2, 1)],
            2: [Vector2(0, 0), Vector2(1, 0), Vector2(1, 1), Vector2(1, 2)],
            3: [Vector2(0, 0), Vector2(0, 1), Vector2(1, 0), Vector2(2, 0)]
        }
        self.move(0, 3)

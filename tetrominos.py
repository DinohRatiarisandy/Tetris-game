"""
    This module contains all tetrominoes and
    all his rotation state
"""


from tetromino import Block
from pygame.math import Vector2

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
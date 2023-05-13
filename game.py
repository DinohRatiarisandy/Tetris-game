"""
    Container for all the elements of Tetris
"""

import pygame, random
from grid import Grid
from tetrominos import *

class Game:
    """Run the game"""

    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.curr_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        """Return a random tetromino"""

        if not self.blocks:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        rand_block = random.choice(self.blocks)
        self.blocks.remove(rand_block)
        return rand_block
    
    def draw(self, SCREEN):
        """Draw the current tetromino on the grid"""

        self.grid.draw(SCREEN)
        self.curr_block.draw(SCREEN)

    def move_left(self):
        """Move the block to the left"""

        self.curr_block.move(0, -1)
        if not self.block_inside():
            self.curr_block.move(0, 1)

    def move_right(self):
        """Move the block to the right"""

        self.curr_block.move(0, 1)
        if not self.block_inside():
            self.curr_block.move(0, -1)        

    def move_down(self):
        """Move the block to the down"""

        self.curr_block.move(1, 0)
        if not self.block_inside():
            self.curr_block.move(-1, 0)
 
    def rotate(self):
        """Rotate the tetrimono"""

        self.curr_block.rotate()
        if not self.block_inside():
            self.curr_block.undo_rotation()
    
    def block_inside(self):
        """Is the block inside the grid ?"""

        tiles = self.curr_block.get_cell_pos()
        for tile in tiles:
            if not self.grid.is_inside(tile.x, tile.y):
                return False
        return True
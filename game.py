"""
    Container for all the elements of Tetris
"""

import random
from grid import Grid
from tetrominos import *

class Game:
    """Run the game"""

    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.curr_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    def update_score(self, line_cleared, move_down_points):
        """add score"""

        if line_cleared==1:
            self.score += 100
        elif line_cleared==2:
            self.score += 300
        elif line_cleared==3:
            self.score += 500
        elif line_cleared==4:
            self.score += 800
        self.score += move_down_points

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
        self.curr_block.draw(SCREEN, 1, 1)

        if self.next_block.id==3:
            self.next_block.draw(SCREEN, 257, 275)
        elif self.next_block.id==2:
            self.next_block.draw(SCREEN, 257, 295)
        else:
            self.next_block.draw(SCREEN, 275, 280)

    def move_left(self):
        """Move the block to the left"""

        self.curr_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():
            self.curr_block.move(0, 1)

    def move_right(self):
        """Move the block to the right"""

        self.curr_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():
            self.curr_block.move(0, -1)

    def move_down(self):
        """Move the block to the down"""

        self.curr_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():
            self.curr_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        """check collision of the last line of the grid
           or another block so show another random block"""
        tiles = self.curr_block.get_cell_pos()
        for pos in tiles:
            self.grid.grid[int(pos.x)][int(pos.y)] = self.curr_block.id
        self.curr_block = self.next_block
        self.next_block = self.get_random_block()

        # check if the one or many rows are full
        row_cleared = self.grid.clear_full_rows()
        self.update_score(row_cleared, 0)
        # check if game over.
        # if the new block doesn't fit in grid, GAME OVER !
        if not self.block_fits():
            if any (self.grid.grid[0][col] for col in range(self.grid.NUM_COLS)):
                self.curr_block.move(-2, 0)
            else:
                self.curr_block.move(-1, 0)
            self.game_over = True

    def block_fits(self):
        """Check if a new block collide with another block"""

        tiles = self.curr_block.get_cell_pos()
        for tile in tiles:
            if not self.grid.is_empty(int(tile.x), int(tile.y)):
                return False
        return True

    def rotate(self):
        """Rotate the tetrimono"""

        self.curr_block.rotate()
        if not self.block_inside() or not self.block_fits():
            self.curr_block.undo_rotation()

    def block_inside(self):
        """Is the block inside the grid ?"""

        tiles = self.curr_block.get_cell_pos()
        for tile in tiles:
            if not self.grid.is_inside(tile.x, tile.y):
                return False
        return True

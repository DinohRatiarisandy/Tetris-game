"""
    This module is for the manipulation of the grid
"""

import pygame, constants

class Grid:
    """Make the grid on the SCREEN"""

    def __init__(self):
        self.NUM_ROWS = 20
        self.NUM_COLS = 10
        self.CELL_SIZE = 30
        self.grid = [[0 for _ in range(self.NUM_COLS)] for _ in range(self.NUM_ROWS)]
        self.colors = constants.COLORS

    def print_grid(self):
        """Print the grid on the console"""

        return print('\n'.join(' '.join(map(str, ans)) for ans in self.grid))
    
    def draw(self, SCREEN):
        """Draw the grid on window"""

        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(
                    self.CELL_SIZE * col + 1,
                    self.CELL_SIZE * row + 1,
                    self.CELL_SIZE - 1,
                    self.CELL_SIZE - 1
                )
                pygame.draw.rect(SCREEN, self.colors[cell_value], cell_rect)

    def is_empty(self, row, col):
        """check if a cell[r][c] is empty"""

        if not self.grid[row][col]:
            return True
        return False
    
    def is_inside(self, row, col):
        """Is the block inside the grid ?"""

        if 0<=row<self.NUM_ROWS and 0<=col<self.NUM_COLS:
            return True
        return False

    def is_row_full(self, row):
        """Check if one row is full"""

        for col in range(self.NUM_COLS):
            if self.grid[row][col]==0:
                return False
        return True

    def clear_row(self, row):
        """clear a full row"""

        for col in range(self.NUM_COLS):
            self.grid[row][col] = 0
    
    def move_row_down(self, row, num_rows):
        """move row down by the number of full rows"""

        for col in range(self.NUM_COLS):
            self.grid[row+num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0
    
    def clear_full_rows(self):
        """Combine check full rows, clear rows and move down"""

        completed = 0
        for row in range(self.NUM_ROWS-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
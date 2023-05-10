"""
    This module is for the manipulation of the grid
"""

import pygame
import constants

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
                    self.CELL_SIZE*col+1,
                    self.CELL_SIZE*row+1,
                    self.CELL_SIZE-1,
                    self.CELL_SIZE-1
                )
                pygame.draw.rect(SCREEN, self.colors[cell_value], cell_rect)
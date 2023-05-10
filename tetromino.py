"""
    This module is the parent of the all blocks
"""


import constants
import pygame

class Block:
    """Class represent one block"""

    def __init__(self, id):
        """id: categorie of the tetromino (L, I, J, O, T, S)"""

        self.id = id
        self.colors = constants.COLORS
        self.cells = {}
        self.CELL_SIZE = 30
        self.rotation = 0
    
    def draw(self, SCREEN):
        """Draw the block with his main color"""

        tiles = self.cells[self.rotation % 4]
        for tile in tiles:
            tile_rect = pygame.Rect(
                tile.y*self.CELL_SIZE+1,
                tile.x*self.CELL_SIZE+1,
                self.CELL_SIZE-1,
                self.CELL_SIZE-1
            )
            pygame.draw.rect(SCREEN, self.colors[self.id], tile_rect)
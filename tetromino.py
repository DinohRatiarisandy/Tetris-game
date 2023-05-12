"""
    This module is the parent of the all blocks
"""

import pygame, constants
from pygame.math import Vector2

class Block:
    """Class represent one block"""

    def __init__(self, id):
        """id: categorie of the tetromino (L, I, J, O, T, S, Z)"""

        self.id = id
        self.colors = constants.COLORS
        self.cells = {}
        self.CELL_SIZE = 30
        self.rotation_state = 0
        self.row_offset = 0
        self.col_offset = 0

    def move(self, row, col):
        """Method to move the tetromino"""

        self.row_offset += row
        self.col_offset += col

    def get_cell_pos(self):
        """Get the current position of one tetromino"""

        tiles = self.cells[self.rotation_state % 4]
        moved_tiles = []

        for pos in tiles:
            moved_tiles.append(
                Vector2(pos.x + self.row_offset, pos.y + self.col_offset)
            )
        return moved_tiles

    def rotate(self):
        """Change the rotation of the tetromino 90 deg"""

        self.rotation_state += 1

    def draw(self, SCREEN):
        """Draw the block with his main color"""

        tiles = self.get_cell_pos()
        for tile in tiles:
            tile_rect = pygame.Rect(
                tile.y * self.CELL_SIZE + 1,
                tile.x * self.CELL_SIZE + 1,
                self.CELL_SIZE - 1,
                self.CELL_SIZE - 1
            )
            pygame.draw.rect(SCREEN, self.colors[self.id], tile_rect)
"""
    This module is the parent of the all blocks
"""


import constants

class Block:
    """Class represent one block"""

    def __init__(self, id):
        """id: categorie of the tetromino (L, I, J, O, T, S ou """

        self.colors = constants.COLORS
        self.cells = dict()
        self.CELL_SIZE = 30
        self.rotation = 0
    
    def draw(self):
        """Draw the block with his main color"""

        

""""
    This module is the main fonction of the game.
    it's make the game playable
"""

import pygame, sys
from grid import Grid
from tetrominos import LBlock

pygame.init()

SCREEN = pygame.display.set_mode((300, 600))
DARK_BLUE = (44, 44, 127)
pygame.display.set_caption("TETRIS")

CLOCK = pygame.time.Clock()

game_grid = Grid()

block = LBlock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(DARK_BLUE)
    game_grid.draw(SCREEN)
    block.draw(SCREEN)

    pygame.display.update()
    CLOCK.tick(60)
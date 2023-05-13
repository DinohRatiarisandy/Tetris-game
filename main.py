""""
    This module is the main fonction of the game.
    it's make the game playable
"""

import pygame, sys
from game import Game

pygame.init()

SCREEN = pygame.display.set_mode((300, 600))
DARK_BLUE = (44, 44, 127)
pygame.display.set_caption("TETRIS")

CLOCK = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 400)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                game.move_left()
            if event.key==pygame.K_RIGHT:
                game.move_right()
            if event.key==pygame.K_DOWN:
                game.move_down()
            if event.key==pygame.K_UP:
                game.rotate()
        if event.type==GAME_UPDATE:
            game.move_down()

    SCREEN.fill(DARK_BLUE)
    game.draw(SCREEN)

    pygame.display.update()
    CLOCK.tick(60)
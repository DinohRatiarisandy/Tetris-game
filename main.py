""""
    This module is the main fonction of the game.
    it's make the game playable
"""

import sys
import pygame
import constants
from game import Game

pygame.init()

game_over_font = pygame.font.Font('./mario_font.ttf', 27)
title_font = pygame.font.Font('./mario_font.ttf', 30)
score_font = pygame.font.Font(None, 57)

score_surface = title_font.render("Score:", True, constants.COLORS['white'])
next_surface = title_font.render('Next:', True, constants.COLORS['white'])
game_over_surface = game_over_font.render('GAME OVER', True, constants.COLORS[5])

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 220, 170, 180)

SCREEN = pygame.display.set_mode((500, 600))
pygame.display.set_caption("TETRIS")

CLOCK = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 250)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if game.game_over:
                new_game = Game()
                game = new_game
            if event.key==pygame.K_LEFT and game.game_over is False:
                game.move_left()
            if event.key==pygame.K_RIGHT and game.game_over is False:
                game.move_right()
            if event.key==pygame.K_DOWN and game.game_over is False:
                game.move_down()
                game.update_score(0, 1)
            if event.key==pygame.K_UP and game.game_over is False:
                game.rotate()
        if event.type==GAME_UPDATE and game.game_over is False:
            game.move_down()

    score_value_surface = score_font.render(str(game.score), True, constants.COLORS['white'])
    SCREEN.fill(constants.COLORS['dark blue'])
    SCREEN.blit(score_surface, (347, 20, 50, 50))
    SCREEN.blit(next_surface, (355, 180, 50, 50))

    if game.game_over:
        SCREEN.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(SCREEN, constants.COLORS['light blue'], score_rect, 0, 10)
    pygame.draw.rect(SCREEN, constants.COLORS['light blue'], next_rect, 0, 10)
    SCREEN.blit(
        score_value_surface,
        score_value_surface.get_rect(
                    centerx=score_rect.centerx,
                    centery=score_rect.centery)
    )
    game.draw(SCREEN)

    pygame.display.update()
    CLOCK.tick(60)

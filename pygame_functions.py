import pygame
from pygame.locals import *
from data import settings
import math

# ------------------------------------------------------------
AUTHORIZED_KEYS = [K_DOWN, K_UP, K_LEFT, K_RIGHT]
WINNING_POS = [str(i) for i in range(
    1, settings['WIDTH_BORDER']*settings['HEIGHT_BORDER'])]+['0']
score = 0
state = 'Theme'


def slide_tiles(settings, game_grid, event):
    zero_index = game_grid.index('0')
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            if zero_index < settings['WIDTH_BORDER']:
                return False
            game_grid[zero_index], game_grid[zero_index - settings['WIDTH_BORDER']
                                             ] = game_grid[zero_index - settings['WIDTH_BORDER']], game_grid[zero_index]
        elif event.key == pygame.K_UP:
            if zero_index >= (settings['HEIGHT_BORDER'] - 1) * settings['WIDTH_BORDER']:
                return False
            game_grid[zero_index], game_grid[zero_index + settings['WIDTH_BORDER']
                                             ] = game_grid[zero_index + settings['WIDTH_BORDER']], game_grid[zero_index]
        elif event.key == pygame.K_RIGHT:
            if zero_index % settings['WIDTH_BORDER'] == 0:
                return False
            game_grid[zero_index], game_grid[zero_index -
                                             1] = game_grid[zero_index - 1], game_grid[zero_index]
        elif event.key == pygame.K_LEFT:
            if (zero_index + 1) % settings['WIDTH_BORDER'] == 0:
                return False
            game_grid[zero_index], game_grid[zero_index +
                                             1] = game_grid[zero_index + 1], game_grid[zero_index]
        return True


def check_win(game_grid, WINNING_POS):
    if game_grid == WINNING_POS:
        return False
    return True


def modify_dynamic_font_size(settings):
    if settings['CELL_SIZE'] < 65:
        return 'SMOL'
    elif settings['CELL_SIZE'] > 65 and settings['CELL_SIZE'] < 135:
        return 'DEFAULT'
    else:
        return 'BIG'


def init_game():
    global score
    score = 0
    game_grid = [str(i) for i in range(
        settings['WIDTH_BORDER']*settings['HEIGHT_BORDER'])]
    settings['CELL_SIZE'] = int(
        math.sqrt((540*540)//(settings['WIDTH_BORDER']*settings['HEIGHT_BORDER'])))
    
    return game_grid


def add_score(score):
    return score+1

def quick_cheat(game_grid):
    game_grid = WINNING_POS
    return game_grid


# ------------------------------------------------------------


def change_grid_size(settings):
    settings['WIDTH_BORDER'] += 1
    settings['HEIGHT_BORDER'] += 1
    if settings['WIDTH_BORDER'] > 10:
        settings['WIDTH_BORDER'] = 3
    if settings['HEIGHT_BORDER'] > 10:
        settings['HEIGHT_BORDER'] = 3
    return settings

def format_grid_size(settings):
    return str(settings['WIDTH_BORDER'])+'x'+str(settings['HEIGHT_BORDER'])
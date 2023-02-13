import pygame
from pygame.locals import *
from data import settings

AUTHORIZED_KEYS = [K_DOWN, K_UP, K_LEFT, K_RIGHT]
WINNING_POS=[str(i) for i in range(1,settings['WIDTH_BORDER']*settings['HEIGHT_BORDER'])]+['0']
score=0
state='Theme'

def ESC_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return False
    return True


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
            
def check_win(game_grid,WINNING_POS):
    if game_grid == WINNING_POS:
        return False
    return True

def add_score(score):
    return score+1

def select_theme_event(event):
    global state
    global current_theme
    if event.type == pygame.KEYDOWN and event.unicode == '1':
        current_theme = 'RETRO'
        state='Menu'
    

def test_run(event):
    global current_theme
    global state
    if event.type == pygame.KEYDOWN and event.unicode == '1':
        current_theme = 'RETRO'
        state='Menu'
    if event.type == pygame.KEYDOWN and event.unicode == '2':
        current_theme = 'CLASSIC'
        state='Menu'
    if event.type == pygame.KEYDOWN and event.unicode == '3':
        current_theme = 'NEON'
        state='Menu'
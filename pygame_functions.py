import pygame
from pygame.locals import *
from data import settings, dump_data, scores
import math
import random

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
    if score > 10:
        game_grid = WINNING_POS
        return game_grid


def change_grid_size(settings):
    settings['WIDTH_BORDER'] += 1
    settings['HEIGHT_BORDER'] += 1
    if settings['WIDTH_BORDER'] > 10:
        settings['WIDTH_BORDER'] = 3
    if settings['HEIGHT_BORDER'] > 10:
        settings['HEIGHT_BORDER'] = 3
    return settings


def format_grid_size(settings):
    return str(settings['WIDTH_BORDER'])+'X'+str(settings['HEIGHT_BORDER'])


def shuffle_grid(game_grid):
    for i in range(len(game_grid)-1, 0, -1):
        j = random.randint(0, i)
        game_grid[i], game_grid[j] = game_grid[j], game_grid[i]
    return game_grid


username = ''
display = ['_']*8


def reset_username():
    global username, display
    username = ''
    display = ['_']*8


def display_username(event, current_theme):
    global username, display
    AUTHORIZED_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    if event.type == pygame.KEYDOWN and current_theme != None:
        if event.key == K_BACKSPACE and len(username) > 0:
            username = username[:-1]
            display[len(username)] = '_'
        if event.unicode in AUTHORIZED_LETTERS and len(username) < 10:
            username += (event.unicode).upper()
            display[len(username)-1] = (event.unicode).upper()


def save_score(scores, username, score):
    if username not in [i for i in scores[format_grid_size(settings)]]:
        scores[format_grid_size(settings)][username] = score
    else:
        if score < scores[format_grid_size(settings)][username]:
            scores[format_grid_size(settings)][username] = score
    dump_data('best_scores', scores)

from pygame_functions import *
from colors import COLORS
import os
from data import settings, scores
import math

pygame.init()
pygame.font.init()

THEME = {
    'RETRO': {
        'BACKGROUND': COLORS['WEIRD_GREEN'],
        'BORDER': COLORS['WEIRD_GREY'],
        'FONTS': {
            'SMOL': pygame.font.Font(os.path.join('fonts', 'Retro_Gaming.ttf'), 20),
            'DEFAULT': pygame.font.Font(os.path.join('fonts', 'Retro_Gaming.ttf'), 30),
            'BIG': pygame.font.Font(os.path.join('fonts', 'Retro_Gaming.ttf'), 80)
        }
    },
    'CLASSIC': {
        'BACKGROUND': COLORS['CLEAR_BLUE'],
        'BORDER': COLORS['BLACK'],
        'FONTS': {
            'SMOL': pygame.font.SysFont('Comic Sans MS', 23),
            'DEFAULT': pygame.font.SysFont('Comic Sans MS', 33),
            'BIG': pygame.font.SysFont('Comic Sans MS', 83)
        }
    },
    'NEON': {
        'BACKGROUND': COLORS['PURPLE'],
        'BORDER': COLORS['LIGHT_BLUE'],
        'FONTS': {
            'SMOL': pygame.font.Font(os.path.join('fonts', 'Neon.ttf'), 20),
            'DEFAULT': pygame.font.Font(os.path.join('fonts', 'Neon.ttf'), 30),
            'BIG': pygame.font.Font(os.path.join('fonts', 'Neon.ttf'), 80)
        }
    },
    'DARK': {
        'BACKGROUND': COLORS['BLACK'],
        'BORDER': COLORS['GREY'],
        'FONTS': {
            'SMOL': pygame.font.Font(os.path.join('fonts', 'Retrolab.ttf'), 20),
            'DEFAULT': pygame.font.Font(os.path.join('fonts', 'Retrolab.ttf'), 30),
            'BIG': pygame.font.Font(os.path.join('fonts', 'Retrolab.ttf'), 100)
        }
    },
}


SCREEN = pygame.display.set_mode((980, 660))
RECTANGLE = pygame.Surface((900, 580))
GAME_DISPLAY = pygame.Surface((860, 540))

current_theme = 'DARK'


def display_select_theme(current_theme):
    theme = THEME[current_theme]
    fonts = theme['FONTS']
    SCREEN.fill(theme['BACKGROUND'])
    SCREEN.blit(RECTANGLE, (40, 40))
    RECTANGLE.fill(theme['BORDER'])
    RECTANGLE.blit(GAME_DISPLAY, (20, 20))
    GAME_DISPLAY.fill(theme['BACKGROUND'])
    GAME_DISPLAY.blit(fonts['BIG'].render(
        'Select Theme:', True, COLORS['WHITE']), (150, 10))
    GAME_DISPLAY.blit(THEME['RETRO']['FONTS']['DEFAULT'].render(
        'Press 1 for Retro', True, COLORS['WHITE']), (250, 250))
    GAME_DISPLAY.blit(THEME['CLASSIC']['FONTS']['DEFAULT'].render(
        'Press 2 for Classic', True, COLORS['WHITE']), (250, 325))
    GAME_DISPLAY.blit(THEME['NEON']['FONTS']['DEFAULT'].render(
        'Press 3 for Neon', True, COLORS['WHITE']), (250, 425))


def draw_menu(current_theme):
    theme = THEME[current_theme]
    fonts = theme['FONTS']
    SCREEN.fill(theme['BACKGROUND'])
    SCREEN.blit(RECTANGLE, (40, 40))
    RECTANGLE.fill(theme['BORDER'])
    RECTANGLE.blit(GAME_DISPLAY, (20, 20))
    GAME_DISPLAY.fill(theme['BACKGROUND'])
    GAME_DISPLAY.blit(fonts['BIG'].render(
        'Puzzle Game', True, COLORS['BLACK']), (100, 10))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Press Enter to start', True, COLORS['BLACK']), (200, 150))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Press Esc to quit', True, COLORS['BLACK']), (200, 200))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Press Backspace to return', True, COLORS['BLACK']), (200, 250))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Press SPACE to change grid size: ', True, COLORS['BLACK']), (200, 300))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(str(settings['WIDTH_BORDER']) +
                      'x'+str(settings['HEIGHT_BORDER']), True, COLORS['BLACK']), (400, 350))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Press * for Scoreboard', True, COLORS['WHITE']), (200, 400))


settings['CELL_SIZE'] = int(
    math.sqrt((540*540)//(settings['WIDTH_BORDER']*settings['HEIGHT_BORDER'])))

game_grid = [str(i) for i in range(
    settings['WIDTH_BORDER']*settings['HEIGHT_BORDER'])]


def draw_grid(settings, game_grid, current_theme, dynamic_font_size):
    theme = THEME[current_theme]
    fonts = theme['FONTS']
    active_font = fonts[dynamic_font_size]
    SCREEN.fill(theme['BACKGROUND'])
    SCREEN.blit(RECTANGLE, (40, 40))
    SCREEN.blit(fonts['DEFAULT'].render(
        'Press TAB to shuffle', True, COLORS['BLACK']), (10, 5))
    SCREEN.blit(fonts['DEFAULT'].render(
        'Press SPACE to quick solve', True, COLORS['BLACK']), (450, 5))
    RECTANGLE.fill(theme['BORDER'])
    RECTANGLE.blit(GAME_DISPLAY, (20, 20))
    GAME_DISPLAY.fill(theme['BACKGROUND'])
    for row in range(settings['HEIGHT_BORDER']):
        for col in range(settings['WIDTH_BORDER']):
            pygame.draw.rect(GAME_DISPLAY, COLORS['BLACK'], (col * settings['CELL_SIZE']+160,
                                                             row * settings['CELL_SIZE'], settings['CELL_SIZE'], settings['CELL_SIZE']), 1)
            if game_grid[row*settings['WIDTH_BORDER']+col] != '0':
                GAME_DISPLAY.blit(active_font.render(game_grid[row*settings['WIDTH_BORDER']+col], True,
                                                     COLORS['BLACK']), (col * settings['CELL_SIZE']+160+20, row * settings['CELL_SIZE']+20))


def draw_win(current_theme, display):
    theme = THEME[current_theme]
    fonts = theme['FONTS']
    SCREEN.fill(theme['BACKGROUND'])
    SCREEN.blit(RECTANGLE, (40, 40))
    RECTANGLE.fill(theme['BORDER'])
    RECTANGLE.blit(GAME_DISPLAY, (20, 20))
    GAME_DISPLAY.fill(theme['BACKGROUND'])
    GAME_DISPLAY.blit(fonts['BIG'].render(
        'You win!', True, COLORS['BLACK']), (150, 50))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Register your name:', True, COLORS['BLACK']), (150, 200))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        ' '.join(display), True, COLORS['BLACK']), (530, 200))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Press TAB to save Username', True, COLORS['BLACK']), (150, 300))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Press Esc to quit', True, COLORS['BLACK']), (150, 350))


def draw_pb(current_theme, display, pB):
    theme = THEME[current_theme]
    fonts = theme['FONTS']
    SCREEN.fill(theme['BACKGROUND'])
    SCREEN.blit(RECTANGLE, (40, 40))
    RECTANGLE.fill(theme['BORDER'])
    RECTANGLE.blit(GAME_DISPLAY, (20, 20))
    GAME_DISPLAY.fill(theme['BACKGROUND'])
    GAME_DISPLAY.blit(fonts['BIG'].render(
        'Scoreboard', True, COLORS['BLACK']), (150, 50))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Press Enter to search your PB', True, COLORS['BLACK']), (150, 300))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Press Esc to quit', True, COLORS['BLACK']), (150, 350))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Press TAB to return', True, COLORS['BLACK']), (150, 400))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        'Press SPACE to change grid size: ', True, COLORS['BLACK']), (150, 450))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(str(settings['WIDTH_BORDER']) +
                      'x'+str(settings['HEIGHT_BORDER']), True, COLORS['BLACK']), (400, 500))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        ' '.join(display), True, COLORS['BLACK']), (150, 200))
    GAME_DISPLAY.blit(fonts['DEFAULT'].render(
        pB, True, COLORS['BLACK']), (450, 200))

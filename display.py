from pygame_functions import *
from colors import COLORS
import os
from data import settings, scores

pygame.init()
pygame.font.init()

THEME={
    "RETRO":{
        "BACKGROUND":COLORS["WEIRD_GREEN"],
        "BORDER":COLORS["WEIRD_GREY"],
        "FONTS":{
                    "SMOL":pygame.font.Font(os.path.join("fonts", "Retro_Gaming.ttf"), 20),
                    "DEFAULT":pygame.font.Font(os.path.join("fonts", "Retro_Gaming.ttf"), 30),
                    "BIG":pygame.font.Font(os.path.join("fonts", "Retro_Gaming.ttf"), 40)
                }
    },
    "CLASSIC":{
        "BACKGROUND":COLORS["CLEAR_BLUE"],
        "BORDER":COLORS["BLACK"],
        "FONTS":{
                    "SMOL":pygame.font.SysFont("Comic Sans MS", 23),
                    "DEFAULT":pygame.font.SysFont("Comic Sans MS", 33),
                    "BIG":pygame.font.SysFont("Comic Sans MS", 43)
                }
    },
    "NEON":{
        "BACKGROUND":COLORS["PURPLE"],
        "BORDER":COLORS["LIGHT_BLUE"],
        "FONTS":{
                    "SMOL":pygame.font.Font(os.path.join("fonts", "Neon.ttf"), 20),
                    "DEFAULT":pygame.font.Font(os.path.join("fonts", "Neon.ttf"), 30),
                    "BIG":pygame.font.Font(os.path.join("fonts", "Neon.ttf"), 40)
                }
    }
}

GAME_VARS={
    "SCORE":0,
    "RUNNING":True,
}

SCREEN = pygame.display.set_mode((980,660))
RECTANGLE = pygame.Surface((900,580))
GAME_DISPLAY=pygame.Surface((860,540))
theme=THEME["RETRO"]
fonts=theme["FONTS"]


def draw_grid(settings):
    SCREEN.blit(RECTANGLE,(40,40))
    RECTANGLE.fill(theme['BORDER'])
    RECTANGLE.blit(GAME_DISPLAY,(20,20))
    GAME_DISPLAY.fill(theme['BACKGROUND'])
    for row in range(settings['HEIGHT_BORDER']):
        for col in range(settings['WIDTH_BORDER']):
            pygame.draw.rect(GAME_DISPLAY, COLORS['BLACK'], (col * settings['CELL_SIZE'], row * settings['CELL_SIZE'], settings['CELL_SIZE'], settings['CELL_SIZE']),1)
            GAME_DISPLAY.blit(fonts['DEFAULT'].render((str(row * settings['HEIGHT_BORDER'] + col)), True, COLORS['BLACK']), (col * settings['CELL_SIZE']+30, row * settings['CELL_SIZE']+30))
    pygame.display.update()
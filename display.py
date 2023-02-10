from pygame_functions import *
from colors import COLORS
import os
from data import settings, scores

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

def create_grid(grid,settings):
    for i in range(settings['HEIGHT_BORDER']):
        grid.append([])
        for j in range(settings['WIDTH_BORDER']):
            grid[i].append(0)
    grid = [[0 for _ in range(settings['WIDTH_BORDER'])]
            for _ in range(settings['HEIGHT_BORDER'])]
    return grid


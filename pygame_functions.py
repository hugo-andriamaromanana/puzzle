import pygame
from pygame.locals import *

def ESC_KEYDOWN(running,event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False
    return running
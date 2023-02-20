from display import *
from keydowns import *


def state_theme_select():
    current_theme = 'DARK'
    display_select_theme(current_theme)


def go_to_menu(current_theme):
    if current_theme != None:
        return 'Menu'


def change_theme(event, current_theme):
    if event.type == pygame.KEYDOWN and event.unicode == '1':
        current_theme = 'RETRO'
    if event.type == pygame.KEYDOWN and event.unicode == '2':
        current_theme = 'CLASSIC'
    if event.type == pygame.KEYDOWN and event.unicode == '3':
        current_theme = 'NEON'
    if event.type == pygame.KEYDOWN and event.unicode == '4':
        current_theme = 'DARK'
    if event.type == pygame.KEYDOWN and event.unicode == '5':
        current_theme = 'FLASH'
    if event.type == pygame.KEYDOWN and event.unicode == '6':
        current_theme = 'WOOD'
    if event.type == pygame.KEYDOWN and event.unicode == '7':
        current_theme = 'FUNKY'
    if event.type == pygame.KEYDOWN and event.unicode == '8':
        current_theme = 'GRANDIOUS'
    return current_theme


pB = 'Search for a user'


def find_PB(username, setting):
    if username in scores[setting]:
        return str(scores[setting][username])
    return 'No PB'


def go_to_menu(current_theme, state):
    if current_theme != None:
        state = 'Menu'
    return state

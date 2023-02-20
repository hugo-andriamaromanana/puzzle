from display import *

# ------------------------------------------------------------


def ESC_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return False
    return True

def SPACEBAR_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        return True

def BACKSPACE_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
        return True

def RETURN_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        return True

def STAR_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_MULTIPLY or event.key == pygame.K_ASTERISK):
        return True

def X_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
        return True

def S_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
        return True

def TAB_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
        return True

# ------------------------------------------------------------
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
    return current_theme

pB='Search for a user'
def find_PB(username,setting):
    if username in scores[setting]:
        return str(scores[setting][username])
    return 'No PB'
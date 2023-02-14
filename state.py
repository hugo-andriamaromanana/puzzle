from display import *

def change_theme(event,current_theme):
    if event.type == pygame.KEYDOWN and event.unicode == '1':
        current_theme = 'RETRO'
    if event.type == pygame.KEYDOWN and event.unicode == '2':
        current_theme = 'CLASSIC'
    if event.type == pygame.KEYDOWN and event.unicode == '3':
        current_theme = 'NEON'
    return current_theme

def return_with_backspace(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
        return True

events=pygame.event.get()
#------------------State---------------------

def state_theme_select():
    current_theme = 'DARK'
    display_select_theme(current_theme)

def go_to_menu(current_theme):
    if current_theme!=None:
        return 'Menu'

def state_theme(state):
    current_theme=None
    state_theme_select()
    for event in events:
        current_theme=change_theme(event,current_theme)
        running = ESC_KEYDOWN(event)
        state=go_to_menu(current_theme)
    return state
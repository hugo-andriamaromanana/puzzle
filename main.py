from display import *

if __name__ == "__main__":
    while GAME_VARS['RUNNING']:
        SCREEN.fill(theme['BACKGROUND'])
        draw_grid(settings)
        for event in pygame.event.get():
            GAME_VARS['RUNNING'] = ESC_KEYDOWN(GAME_VARS['RUNNING'],event)
        pygame.display.update()

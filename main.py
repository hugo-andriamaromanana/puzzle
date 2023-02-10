from display import *

pygame.init()

GAME_VARS={
    "GRID":create_grid([],settings),
    "SCORE":0,
    "BEST_SCORE":scores['BEST_SCORE'],
}

screen = pygame.display.set_mode(980,660)
DISPLAYSURF = pygame.display.set_mode((980, 660))

if __name__ == "__main__":
    running=True
    while running:
        screen.fill(THEME[settings['THEME']]['BACKGROUND'])
        for event in pygame.event.get():
            running = ESC_KEYDOWN(running,event)
        pygame.display.update()

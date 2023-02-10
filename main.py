from display import *

if __name__ == "__main__":
    WINNING_POS=[str(i) for i in range(1,settings['WIDTH_BORDER']*settings['HEIGHT_BORDER'])]+['0']
    running=True
    while running: 
        draw_grid(settings,game_grid)
        events=pygame.event.get()
        for event in events:
            running = ESC_KEYDOWN(event)
            if slide_tiles(settings,game_grid,event):
                draw_grid(settings,game_grid)
            if not check_win(game_grid,WINNING_POS):
                running=False
            #------------------------------------------------------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_grid = ['1', '2', '3', '4', '5', '6', '7', '0', '8']
            #------------------------------------------------------------
        pygame.display.update()

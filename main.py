from display import *

if __name__ == "__main__":
    running=True
    while running: 
        draw_grid(settings,game_grid)
        events=pygame.event.get()
        for event in events:
            running = ESC_KEYDOWN(event)
            if slide_tiles(settings,game_grid,event):
                draw_grid(settings,game_grid)
                score=add_score(score)
            if not check_win(game_grid,WINNING_POS):
                running=False
            #------------------------------------------------------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_grid = ['1', '2', '3', '4', '5', '6', '7', '0', '8']
            #------------------------------------------------------------
        pygame.display.update()

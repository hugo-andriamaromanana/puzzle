from display import *

if __name__ == "__main__":
    running=True
    while running:
        events=pygame.event.get()
        if state=='Theme':
            display_select_theme(current_theme)
            for event in events:
                test_run(event)
                running = ESC_KEYDOWN(event)
        if state=='Menu':
            draw_menu(current_theme)
            for event in events:
                running = ESC_KEYDOWN(event)
        if state=='Game':
            draw_grid(settings,game_grid)
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

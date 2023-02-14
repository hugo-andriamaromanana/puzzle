from state import *

if __name__ == "__main__": 
    state='Theme'
    running=True
    current_theme=None
    while running:
        events=pygame.event.get()
        if state=='Theme':
            current_theme=None
            state_theme_select()
            for event in events:
                current_theme=change_theme(event,current_theme)
                running = ESC_KEYDOWN(event)
                if current_theme!=None:
                    state='Menu'
        if state=='Menu':
            draw_menu(current_theme)
            for event in events:
                running = ESC_KEYDOWN(event)
                if return_with_backspace(event):
                    state='Theme'
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    state='Game'
                    game_grid = init_game()
        if state=='Game':
            draw_grid(settings,game_grid,current_theme)
            for event in events:
                running = ESC_KEYDOWN(event)
                if slide_tiles(settings,game_grid,event):
                    draw_grid(settings,game_grid,current_theme)
                    score=add_score(score)
                if not check_win(game_grid,WINNING_POS):
                    state='Menu'
                #------------------------------------------------------------
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_grid = ['1', '2', '3', '4', '5', '6', '7', '0', '8']
                #------------------------------------------------------------
        pygame.display.update()
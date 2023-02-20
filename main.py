from state import *

if __name__ == '__main__':
    state = 'Theme'
    running = True
    while running:
        events = pygame.event.get()
        if state == 'Theme':
            current_theme = None
            state_theme_select()
            for event in events:
                current_theme = change_theme(event, current_theme)
                running = ESC_KEYDOWN(event)
                state = go_to_menu(current_theme, state)
        if state == 'Menu':
            draw_menu(current_theme)
            for event in events:
                running = ESC_KEYDOWN(event)
                if BACKSPACE_KEYDOWN(event):
                    state = 'Theme'
                if RETURN_KEYDOWN(event):
                    game_grid = init_game()
                    WINNING_POS = [str(i) for i in range(
                        1, settings['WIDTH_BORDER']*settings['HEIGHT_BORDER'])]+['0']
                    dynamic_font_size = modify_dynamic_font_size(settings)
                    state = 'Game'
                if SPACEBAR_KEYDOWN(event):
                    settings = change_grid_size(settings)
                if STAR_KEYDOWN(event):
                    state = 'PB'
        if state == 'Game':
            draw_grid(settings, game_grid, current_theme, dynamic_font_size)
            for event in events:
                running = ESC_KEYDOWN(event)
                if slide_tiles(settings, game_grid, event):
                    draw_grid(settings, game_grid,
                              current_theme, dynamic_font_size)
                    score = add_score(score)
                if not check_win(game_grid, WINNING_POS):
                    state = 'Win'
                if BACKSPACE_KEYDOWN(event):
                    state = 'Menu'
                if TAB_KEYDOWN(event):
                    game_grid = shuffle_grid(game_grid)
                    score = 0
                if SPACEBAR_KEYDOWN(event):
                    game_grid = WINNING_POS
                    draw_grid(settings, game_grid,
                              current_theme, dynamic_font_size)
        if state == 'Win':
            draw_win(current_theme, display)
            for event in events:
                running = ESC_KEYDOWN(event)
                display_username(event, current_theme)
                if TAB_KEYDOWN(event):
                    save_score(
                        scores, (''.join([i for i in display if i != '_'])), score)
                    score = 0
                    game_grid = init_game()
                    state = 'Menu'
        if state == 'PB':
            draw_pb(current_theme, display, pB)
            for event in events:
                display_username(event, current_theme)
                running = ESC_KEYDOWN(event)
                if RETURN_KEYDOWN(event):
                    pB = find_PB(
                        (''.join([i for i in display if i != '_'])), format_grid_size(settings))
                if TAB_KEYDOWN(event):
                    state = 'Menu'
                if SPACEBAR_KEYDOWN(event):
                    settings = change_grid_size(settings)
        pygame.display.update()

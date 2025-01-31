import pygame 
from .board import Board

SIZE_TILE=100

def start() -> None : 

    pygame.init()
    screen_size = (300,300)
    board=Board.config()
    screen=pygame.display.set_mode(screen_size)

    while True : 

        for event in pygame.event.get() :
            # Closing window (Mouse click on cross icon or OS keyboard shortcut)
            if event.type == pygame.QUIT:
                pygame.quit()
            
        board.draw(screen, SIZE_TILE)


            

        # Display
        pygame.display.update()
    #pygame.quit

def start_play() -> None : 

    pygame.init()
    screen_size = (300,300)
    board=Board.config()
    screen=pygame.display.set_mode(screen_size)

    while True : 

        for event in pygame.event.get() :
            # Closing window (Mouse click on cross icon or OS keyboard shortcut)
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN: #on regarde s'il y a un déplacement
            if event.key == pygame.K_q: 
                running = False
            if event.key == pygame.K_UP and direction != (0,1): #on fait pas demi tour
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0,-1): #on fait pas demi tour
                direction = (0, 1)
            elif event.key == pygame.K_RIGHT and direction != (-1,0): #on fait pas demi tour
                direction = (1, 0)
            elif event.key == pygame.K_LEFT and direction != (1,0): #on fait pas demi tour
                direction = (-1, 0)
            
        board.draw(screen, SIZE_TILE)


            

        # Display
        pygame.display.update()
    #pygame.quit

def start_auto() -> None : 

    pygame.init()
    screen_size = (300,300)
    board=Board.config()
    screen=pygame.display.set_mode(screen_size)

    while True : 

        for event in pygame.event.get() :
            # Closing window (Mouse click on cross icon or OS keyboard shortcut)
            if event.type == pygame.QUIT:
                pygame.quit()
            
        board.draw(screen, SIZE_TILE)


            

        # Display
        pygame.display.update()
    #pygame.quit
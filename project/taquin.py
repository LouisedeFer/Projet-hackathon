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
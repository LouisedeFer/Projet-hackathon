import pygame 
from .board import Board
from .dir import Dir

SIZE_TILE=100

running = True
def start_play() -> None : 

    pygame.init()
    screen_size = (300,300)
    board=Board.config()
    screen=pygame.display.set_mode(screen_size)

    while running : 

        for event in pygame.event.get() :
            # Closing window (Mouse click on cross icon or OS keyboard shortcut)
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN: #on regarde s'il y a un déplacement ou fermeture d'appli
                if event.key == pygame.K_q: 
                    running = False

                if event.key == pygame.K_UP:
                    board.movement(Dir.UP)
                elif event.key == pygame.K_DOWN:
                    board.movement(Dir.DOWN)
                elif event.key == pygame.K_RIGHT:
                    board.movement(Dir.RIGHT)
                elif event.key == pygame.K_LEFT:
                    board.movement(Dir.LEFT)

        board.draw(screen, SIZE_TILE)

            

        # Display
        pygame.display.update()
    #pygame.quit

def start_auto() -> None : 

    pygame.init()
    screen_size = (300,300)
    board=Board.config()
    screen=pygame.display.set_mode(screen_size)

    while running : 

        for event in pygame.event.get() :
            # Closing window (Mouse click on cross icon or OS keyboard shortcut)
            if event.type == pygame.QUIT:
                pygame.quit()
            
        board.draw(screen, SIZE_TILE)


            

        # Display
        pygame.display.update()
    #pygame.quit
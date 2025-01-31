import pygame 
from .board import Board
from .tile import Tile
from .solver import solve
from .dir import Dir

SIZE_TILE = 100
NB_LINES = 3
NB_COLS = 3

def start_play() -> None : 

    pygame.init()
    screen_size = (300,300)
    board=Board.config()
    screen=pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    while True : 

        clock.tick(10)
        for event in pygame.event.get() :
            # Closing window (Mouse click on cross icon or OS keyboard shortcut)
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN: #on regarde s'il y a un déplacement ou fermeture d'appli
                if event.key == pygame.K_q: 
                    pygame.quit()

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
    clock = pygame.time.Clock()

    solution_board = [[0 for j in range(NB_COLS)]for i in range(NB_LINES)]
    for i in range(NB_LINES):
        for j in range(NB_COLS):
            solution_board[i][j]=str(i*NB_COLS + j + 1)
    solution_board[-1][-1]="-"
    solution = Board.config(solution_board)

    result = solve(board, solution)

    for k in range(len(result)): 

        clock.tick(1)

        for event in pygame.event.get() :
            # Closing window (Mouse click on cross icon or OS keyboard shortcut)
            if event.type == pygame.QUIT:
                pygame.quit()
        
        board = result[k]
        print("solution")
        print(board)

        board.draw(screen, SIZE_TILE)

        # Display
        pygame.display.update()

    pygame.quit
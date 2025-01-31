from .tile import Tile 
from .dir import Dir

import numpy as np
import pygame as pg
from dir import Dir

### DEFAULT CONSTANTS

NB_LINES = 3
NB_COLS = 3
COLOR = pg.Color("blue")
TILE_SIZE=100

class Board:
    def __init__(self, board):
        self._board = board
        self._nb_cols = len(self._board[0])
        self._nb_lines = len(self._board)

    def __repr__(self):
        for i in range(self._nb_lines):
            for j in range(self._nb_cols):
                print(self._board[i][j].number, end = ' ')
            print()
        
    def __equals__(self, other):
        indic = True
        for i in range(3):
            for j in range(3):
                if self._board[i][j].number != other.board[i][j].number:
                    indic = False
        return indic

    def allowed_moves(self) -> list[Dir]:
        "Return a list of all the playable moves in a given configuration."
        L= [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]
        minus_position = self.minus_position()
        i = minus_position[0]
        j = minus_position[0]
        if i == 0:
            L.remove(Dir.UP)
        if i == self._nb_lines -1:
            L.remove(Dir.DOWN)
        if j == 0:
            L.remove(Dir.LEFT)
        if j == self._nb_cols -1:
            L.remove(Dir.RIGHT)
        return L
        
    @classmethod
    def config(cls):
        # generate a random configuration of the board
        L = []
        for i in range(1, NB_LINES*NB_LINES):
            L.append(f'{i}')
        L.append('-') # list of integers and a '-'
        tab = np.array(L).reshape(NB_LINES,NB_COLS) # transforming it into a table '-'
        np.random.shuffle(tab) # and then shuffling it 

        # same thing with tiles objects
        board = [[0 for i in range(NB_LINES)] for j in range(NB_COLS)]
        for i in range(NB_LINES):
            for j in range(NB_COLS):
                board[i][j] = Tile(i, j, COLOR, tab[i][j])
        return cls(board)
    
    def movement(self, direction : Dir) -> "Board":
        # change the position of '-' depending on the direction
        new = self._board
        x, y = self.minus_position()

        if direction == Dir.UP and x > 0:
            new[x][y], new[x-1][y] = new[x-1][y], new[x][y]
        elif direction == Dir.DOWN and x < 2:
            new[x][y], new[x+1][y] = new[x+1][y], new[x][y]
        elif direction == Dir.LEFT and y > 0:
            new[x][y], new[x][y-1] = new[x][y-1], new[x][y]
        elif direction == Dir.RIGHT and y < 2:
            new[x][y], new[x][y+1] = new[x][y+1], new[x][y]
        
        return Board(new)

    def minus_position(self) -> tuple[int, int]:
        # cherche la posiiton du "-" dans le board
        for i in range(self._nb_lines):
            for j in range(self._nb_cols):
                if self._board[i][j].number == '-':
                    return i, j


    def draw(self, screen : pg.Surface, size : int) :
        for liste in self._board :
            for elt in liste : 
                elt.draw(screen, TILE_SIZE)

    @property
    def board(self):
        return self._board
    
    





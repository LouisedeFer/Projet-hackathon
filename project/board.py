from .tile import Tile 
from .dir import Dir

import numpy as np
import pygame as pg


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

    def __repr__(self)->str:
        s = ""
        for i in range(self._nb_lines):
            for j in range(self._nb_cols):
                s += str(self._board[i][j].number)
            #s += "\n"
        return s
        
    def __equals__(self, other):
        indic = True
        for i in range(3):
            for j in range(3):
                if self._board[i][j].number != other._board[i][j].number:
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
    def config(cls, L : list[str] |None= None):
        # generate a random configuration of the board
        if L is None:
            L = []
            for i in range(1, NB_LINES*NB_LINES):
                L.append(f'{i}')
            L.append('-') # list of integers and a '-'
            tab = np.array(L).reshape(NB_LINES,NB_COLS) # transforming it into a table '-'
            np.random.shuffle(tab) # and then shuffling it 
        else:
            tab = np.array(L).reshape(NB_LINES,NB_COLS) # transforming it into a table '-'

        # same thing with tiles objects
        board = [[0 for i in range(NB_LINES)] for j in range(NB_COLS)]
        for i in range(NB_LINES):
            for j in range(NB_COLS):
                board[i][j] = Tile(i, j, COLOR, tab[i][j])

        return cls(board)
    
    def movement(self, direction : Dir) -> None:
        # change the position of '-' depending on the direction
        i, j = self.minus_position()
        print((i,j))

        if direction == Dir.UP and i > 0:
            self._board[i][j], self._board[i-1][j] = self._board[i-1][j], self._board[i][j]
            print(self)

        elif direction == Dir.DOWN and i < 2:
            self._board[i][j], self._board[i+1][j] = self._board[i+1][j], self._board[i][j]
        elif direction == Dir.LEFT and j > 0:
            self._board[i][j], self._board[i][j-1] = self._board[i][j-1], self._board[i][j]
        elif direction == Dir.RIGHT and j < 2:
            self._board[i][j], self._board[i][j+1] = self._board[i][j+1], self._board[i][j]



        

    def minus_position(self) -> tuple[int, int]:
        # cherche la posiiton du "-" dans le board
        pos : tuple[int,int]| None = None
        for i in range(self._nb_lines):
            for j in range(self._nb_cols):
                if self._board[i][j].number == '-':
                    pos= (j, i)
                    break 

        if pos is None :
            raise Exception("hole not found")
        return pos


    def draw(self, screen : pg.Surface, size : int) :
        for liste in self._board :
            for elt in liste : 
                elt.draw(screen, TILE_SIZE)
    
    





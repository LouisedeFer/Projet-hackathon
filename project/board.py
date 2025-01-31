from .tile import Tile 
from .dir import Dir

import numpy as np
import pygame as pg
from dir import Dir


COLOR = pg.Color("blue")
TILE_SIZE=100

class Board:
    def __init__(self, board, nb_lines, nb_cols):
        self._board = board
        self._nb_lines = nb_lines
        self._nb_cols = nb_cols

    def __repr__(self):
        for i in range(self._nb_lines):
            for j in range(self._nb_cols):
                print(self._board[i][j].number, end = ' ')
            print()

    def allowed_moves(self) -> List[Dir]:
        "Return a list of all the playable moves in a given configuration."
        L= [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]
        minus_position = self.get_minus()
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
        # on génère une configuration aléatoire de chiffres pour le board
        L = []
        for i in range(1, self._nb_lines*self._nb_cols):
            L.append(f'{i}')
        L.append('-') # liste des chiffres et du '-'
        tab = np.array(L).reshape(self._nb_lines,self._nb_cols) # tableau des chiffres et du '-'
        np.random.shuffle(tab) # tableau des chiffres et du '-' mélangée

        # on fait la même chose avec des objets tiles
        board = [[0 for i in range(nb_lines)] for j in range(nb_cols)]
        for i in range(nb_lines):
            for j in range(nb_cols):
                board[i][j] = Tile(i, j, COLOR, tab[i][j]) # même chose mais composé de tiles
        return cls(board)
    
    def movement(self, direction : Dir):
        # change la position du '-' en fonction de la direction
        new = self._board
        x, y = self.position()

        if direction == Dir.UP:
            new[x][y], new[x-1][y] = new[x-1][y], new[x][y]
        elif direction == Dir.DOWN:
            new[x][y], new[x+1][y] = new[x+1][y], new[x][y]
        elif direction == Dir.LEFT:
            new[x][y], new[x][y-1] = new[x][y-1], new[x][y]
        elif direction == Dir.RIGHT:
            new[x][y], new[x][y+1] = new[x][y+1], new[x][y]
        
        return Board(new)

    def position(self):
        # cherche la posiiton du "-" dans le board
        for i in range(3):
            for j in range(3):
                if self._board[i][j].number == '-':
                    return i, j


    def draw(self, screen : pg.Surface, size : int) :
        for liste in self._board :
            for elt in liste : 
                elt.draw(screen, TILE_SIZE)
    
    





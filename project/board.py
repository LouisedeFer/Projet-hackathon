from .tile import Tile 
from .dir import Dir
import numpy as np
import pygame as pg

COLOR = pg.Color("blue")
TILE_SIZE=100

class Board:
    def __init__(self, board):
        self._board = board

    def __repr__(self):
        for i in range(3):
            for j in range(3):
                print(self._board[i][j].number, end = ' ')
            print()

    @classmethod
    def config(cls):
        # on génère une configuration aléatoire de chiffres pour le board
        L = []
        for i in range(1, 9):
            L.append(f'{i}')
        L.append('-') # liste des chiffres et du '-'
        tab = np.array(L).reshape(3,3) # tableau des chiffres et du '-'
        np.random.shuffle(tab) # tableau des chiffres et du '-' mélangée

        # on fait la même chose avec des objets tiles
        board = [[0 for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                board[i][j] = Tile(i, j, COLOR, tab[i][j]) # même chose mais composé de tiles
        return cls(board)

    def draw(self, screen : pg.Surface, size : int) :
        for liste in self._board :
            for elt in liste : 
                elt.draw(screen, TILE_SIZE)
    
    





from tile import Tile 
import numpy as np
import pygame as pg

COLOR = pg.Color("blue")

class Checkerboard:
    def __init__(self):
        # on génère une configuration aléatoire de tile pour le board
        L = []
        for i in range(1, 9):
            L.append(f'{i}')
        L.append('-')
        L = np.random.choice(L, (3,3)) # liste des chiffres et du '-'

        board = [[0 for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                board[i][j] = Tile(i, j, COLOR, L[i][j]) # même chose mais composé de tiles
        self.board = board

    def __repr__(self):
        board = Checkerboard()
        for i in range(3):
            for j in range(3):
                print(board.board[i][j].number, end = ' ')
            print()






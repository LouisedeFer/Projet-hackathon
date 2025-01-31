import project
import pygame


board=project.Board.config()

print(board)
L=[str(i) for i in range(1,9)]
L.append("-")

def test_board_1() :
    board=project.Board.config(L)
    assert str(board)=="12345678-"
    board.movement(project.Dir.UP)
    assert str(board)=="12345-786"

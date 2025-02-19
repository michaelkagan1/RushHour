'''
Helper functions to check RushHour game board, find possible moves, return new boards, etc.

Numbers represent cars. car #1 is always the car that needs to escape and is always in the 3rd row.
'''
import numpy as np
from copy import deepcopy
from data_struct import Board, Car, Node, QueueFrontier

def test(arr):
    board = board_from_array(arr)
    print(board)
    board.move_car(board.cars[2], -1)
    print('\n',board)
    board.move_car(board.cars[4], -3)
    print('\n',board)
    board.move_car(board.cars[3], 3)
    print('\n',board)

# Example board:
b0 = [
 [0,0,2,0,3,3],
 [0,0,2,0,0,0],
 [1,1,2,0,0,0],
 [4,4,4,0,0,5],
 [0,0,0,0,0,5],
 [0,0,0,0,0,5]
 ]

# Example board:
b1 = [
 [0,0,2,0,0,0],
 [0,0,2,0,0,0],
 [0,0,2,0,0,0],
 [0,0,0,0,0,0],
 [0,0,0,0,0,0],
 [0,0,0,0,0,0]
 ]

#convert matrix to board object with numbered car objects
def board_from_array(array):
    array = np.array(array)
    numbers = set(array.ravel())
    numbers.pop()   # removes 0 from set because 0 is not a car
    board = Board()
    for num in numbers:
        rows, cols = np.where(array==num)
        coord = list(zip(rows,cols))
        x = Car(coord, num, isMain=(num == 1))
        board.add_car(car=x)
    return board

# possible moves
def possible_moves(board):
    moves = dict()
    for car in board.cars:
        pass
        



# movable pieces

# resulting board

# Winning position is one where
# terminal board -> boolean

if __name__ == '__main__':
    test(b0)
'''
Helper functions to check RushHour game board, find possible moves, return new boards, etc.

Numbers represent cars. car #1 is always the car that needs to escape and is always in the 3rd row.
'''
import numpy as np
from copy import deepcopy
from data_struct import Board, Car

def test(arr):
    board = board_from_array(arr)
    print(board)

    new_board = board.move_car(board.cars[2], -1)
    print('\n',board)
    # board.move_car(board.cars[4], -3)
    # print('\n',board)
    # board.move_car(board.cars[3], 3)
    # print('\n',board)

    # moves = board.empty_neighbors.copy()
    # print(f'Befoe pop: {board.empty_neighbors}')
    # moves.pop(board.cars[0])
    # print(f'After pop: {board.empty_neighbors}')

# Example board:
b1 = [
 [0,0,2,0,3,3],
 [0,0,2,0,0,0],
 [1,1,2,0,0,0],
 [4,4,4,0,0,5],
 [0,0,0,0,0,5],
 [0,0,0,0,0,5]
 ]

b2 = [
 [0,0,2,0,0,0],
 [0,0,2,0,0,3],
 [0,0,2,1,1,3],
 [4,4,4,5,0,3],
 [0,0,0,5,6,6],
 [0,0,0,0,0,0]
 ]

b40 = [
 [2,3,3,4,4,4],
 [2,0,5,5,6,0],
 [1,1,7,0,6,0],
 [8,8,7,9,9,10],
 [0,11,11,12,0,10],
 [13,13,13,12,0,10]
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
    return board.empty_neighbors 

# resulting board

# Winning position is one where
# terminal board -> boolean

if __name__ == '__main__':
    test(b0)
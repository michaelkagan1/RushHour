'''
A 2D array is used to represent the board at the simplest level. 0s are empty spaces. All other cars have non-zero integers. 
Car #1 is always the "red" car, or the car that needs to escape to the right side of the board, always in the 3rd row. 

This file contains 3 example boards for validating search algorithm. b1 and b2 are the first 2 boards in the actual RushHour game, and the easiest levels. 
b40 is the last problem and the most difficult level. 
'''
import numpy as np
from copy import deepcopy
from data_struct import Board, Car

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
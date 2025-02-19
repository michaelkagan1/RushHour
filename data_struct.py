import numpy as np

class Board():
    '''
    board object which contains cars and represents a board in RushHour
    '''
    def __init__(self):
        self.cars = []
        
    def add_car(self, car):
        self.cars.append(car)

    def move_car(self, car, action):
        coords = car.coord
        if car.orientation == 'vert':
            coords = [(x+action, y) for x,y in coords]
        if car.orientation == 'horiz':
            coords = [(x,y+action) for x,y in coords]
        car.coord = coords

    def __str__(self):
        # print function for printing array (use zeros array, then populate with coords)
        array = np.zeros([6,6]) #2d array
        for car in self.cars:
            for i,j in car.coord:
                array[i][j] = car.name
        return str(array)


class Car():
    '''
    car object for use in RushHour Board object
    coordinates is a list of tuples in matrix notation (i,j) identifying position of cars
    isMain is True only for one car per board - used for main (red) car that needs to escape
    orientation is vertical or horizontal depending on the coordinates and determines how cars can move
    '''
    def __init__(self, coord, name, isMain=False):
        self.coord = coord
        self.name = name
        self.main = isMain
        self.orientation = self.get_orientation(coord) # -> 'vert' | 'horiz'

    def get_orientation(self,coord):
        # handle exceptions in identifying car orientation. Checks on coordinates
        if len(coord)<2 or len(coord)>3:    # check car length
            raise Exception('Invalid car length') 
        # handle tuple format (i,j)
        if any([len(tup)!=2 for tup in coord]):
            raise Exception('Invalid coordinate tuple format')
        # handle tuple indices
        if any([i not in range(6) for i,j in coord]) or any([j not in range(6) for i,j in coord]):
            raise Exception('Invalid coordinate index')

        if len(set([i for i,j in coord])) == 1:
             return 'horiz'
        elif len(set([j for i,j in coord])) == 1:
            return 'vert'
        else: 
            raise Exception('Invalid car coordinates')


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class QueueFrontier():
    def __init__(self):
        self.frontier = []
        self.memo = []

    def isEmpty(self):
        return len(self.frontier) == 0

    # add node to frontier to be searched. Add board to persistent 'memo' list
    def enqueue(self, node):
        self.frontier.append(node)
        self.memo.append(node.state)

    def dequeue(self):
        if not self.isEmpty():
            return self.frontier.pop(0)
        raise Exception('Empty frontier: cannot dequeue node')

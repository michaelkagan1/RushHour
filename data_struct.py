import numpy as np

class Board():
    '''
    board object which contains cars and represents a board in RushHour
    state is the array representing the board
    cars is a list of car objects
    empty neighbors is a dict tying each car to the available steps it can take in it's dimension 
    '''
    def __init__(self):
        self.state = np.zeros([6,6])
        self.cars = []
        self.empty_neighbors = dict()
        
    def add_car(self, car):
        self.cars.append(car)
        self.update_board_state()

    def update_board_state(self):
        array = np.zeros([6,6]) #2d array
        for car in self.cars:
            for i,j in car.coord:
                array[i][j] = car.name
        self.state = array

        # update empty neighbors dict 
        for car in self.cars:
            # list of available spaces adjacent to car in cars orientation 
            empty_neighbors = []
            if car.orientation == 'vert':
                # get first, last coordinate; check all spaces behind, and infront, until hitting border or taken space
                j = car.coord[0][1]
                first = min([i for i,j in car.coord])
                i = -1
                while first + i >= 0 and self.state[first+i][j]==0: # while not hitting border, and space is available
                    empty_neighbors.append(i)
                    i-=1
                last = max([i for i,j in car.coord])
                i = 1
                while last + i < 6 and self.state[last+i][j]==0: # while not hitting border, and space is available
                    empty_neighbors.append(i)
                    i+=1
            elif car.orientation == 'horiz':
                # get first, last coordinate; check all spaces behind, and infront, until hitting border or taken space
                i = car.coord[0][0]
                first = min([j for i,j in car.coord])
                j = -1
                while first + j >= 0 and self.state[i][first+j]==0: # while not hitting border, and space is available
                    empty_neighbors.append(j)
                    j-=1
                last = max([j for i,j in car.coord])
                j = 1
                while last + j < 6 and self.state[i][last+j]==0: # while not hitting border, and space is available
                    empty_neighbors.append(j)
                    j+=1
            self.empty_neighbors[car] = empty_neighbors

    def move_car(self, car, action):
        if action not in self.empty_neighbors[car]:
            raise Exception(f'Invalid move by {car.name}: space taken')

        coords = car.coord

        if car.orientation == 'vert':
            new_coords = [(x+action, y) for x,y in coords]
        if car.orientation == 'horiz':
            new_coords = [(x,y+action) for x,y in coords]

        car.coord = new_coords
        
        # update board state if any car moves
        self.update_board_state()
    
    def winning_state(self):
        main_car = self.cars[0]
        assert(main_car.name == 1)
        farthest_y = max([j for i,j in main_car.coord])

        row = self.state[2]         # main car always in 3rd row
        row = row[farthest_y+1:]    # row values for index after main car to end of row
        return not any(row)         # if any numbers not 0, it returns False

    def __str__(self):
        # print function for printing array (use zeros array, then populate with coords)
        return str(self.state)


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
        # self.memo = []
        self.memo = set()

    def isEmpty(self):
        return len(self.frontier) == 0
    
    def explored(self, array):
        return array.tobytes() in self.memo
        # for board in self.memo:
        #     if np.array_equal(board, array):
        #         return True
        # return False

    # add node to frontier to be searched. Add board to persistent 'memo' list
    def enqueue(self, node):
        self.frontier.append(node)
        self.memo.add(node.state.state.tobytes())  # node state is board object, board object state is 2D-array. Convert to bytes before adding for optimization

    def dequeue(self):
        if not self.isEmpty():
            return self.frontier.pop(0)
        raise Exception('Empty frontier: cannot dequeue node')


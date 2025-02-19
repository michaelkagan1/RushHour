from data_struct import Node, QueueFrontier
import time
from copy import deepcopy
from helpers import *


def solve(board):
    counter = 0

    # make starting node with board
    start_board = board_from_array(board)
    start_node = Node(start_board, parent=None, action=None)

    # add starting node to frontier
    frontier = QueueFrontier()
    frontier.enqueue(start_node)

    winning_node = None

    # start inf loop
    while True:
        
        if frontier.isEmpty():
            break

        # dequeue node and set to current node
        current_node = frontier.dequeue()

        # check if node is terminal state, if it is then save and break out of inf loop
        if current_node.state.winning_state():
            winning_node = current_node
            break

        # obtain all possible moves dict
        current_moves_dict = current_node.state.empty_neighbors
        moves = [(car,action) for car,actions in current_moves_dict.items() for action in actions]

        # loop over possible moves
        for car,action in moves:
            counter += 1
            # get current and next move options without the current car and compare the two dicts. If identical, the action is not productive (a car going back and forth)
            current_moves_dict_copy = current_moves_dict.copy()

            # remove car in question from copy to compare with moves dict after moving the car
            current_moves_dict_copy.pop(car)

            # new_board = deepcopy(current_node.state).move_car(car,action)
            current_node.state.move_car(car,action)
            new_moves_dict = current_node.state.empty_neighbors.copy()
            new_moves_dict.pop(car)

            # If move produces a different set of possible moves (if it is a "productive" move) optimization
            if not current_moves_dict == new_moves_dict:

                # If not in previously seen boards in frontier
                if not frontier.explored(current_node.state.state):
                # get resulting board, put it in new node in frontier, and in seen list
                    frontier.enqueue(Node(deepcopy(current_node.state), current_node, (car,action)))
            
            # move car back to where it came from for next iter in for loop
            current_node.state.move_car(car, action*(-1))

    if winning_node == None:
        print('No solution')
        return []

    # backtrack to until node who's parent is None, return nodes actions
    else:
        solution = []
        node = winning_node
        while node.action != None:
            solution.append((node.action[0].name, node.action[1]))
            node = node.parent

    solution.reverse()
    print('Solution converged', '\n', f'{counter} positions scanned', '\n')
    print(solution)
    return solution

if __name__ == '__main__':
    t0 = time.time()
    solve(b40)
    t1 = time.time()
    print('\n', t1-t0, ' seconds')
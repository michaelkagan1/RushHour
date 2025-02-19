from data_struct import Node, QueueFrontier
from helpers import *

# make starting node with board

# add starting node to frontier

# start inf loop

    # loop over each node in frontier

    # check if node is terminal state, if it is then save and break out of inf loop

    # dequeue node and set to current node

    # obtain all possible moves

    # loop over possible moves

        # if move produces a different set of possible moves (if it is a "productive" move) and if it's not in previously seen boards in frontier

        # get resulting board, put it in new node in frontier, and in seen list

# backtrack to first node who's grandparent (node.parent.parent) is None, return that nodes action

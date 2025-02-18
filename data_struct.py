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

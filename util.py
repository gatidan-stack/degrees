# util.py
from collections import deque

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class Frontier:
    """
    Base class for StackFrontier and QueueFrontier.
    """
    def __init__(self):
        self.frontier = deque()
        self.frontier_states = set()  # O(1) lookup for contains_state

    def add(self, node):
        self.frontier.append(node)
        self.frontier_states.add(node.state)

    def contains_state(self, state):
        return state in self.frontier_states

    def empty(self):
        return len(self.frontier) == 0

    def remove_front(self):
        """
        Removes and returns the first element.
        This method is used by QueueFrontier.
        """
        if self.empty():
            raise Exception("empty frontier")
        node = self.frontier.popleft()
        self.frontier_states.remove(node.state)
        return node


class StackFrontier(Frontier):
    """
    Frontier for Depth-First Search (LIFO).
    """
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        node = self.frontier.pop()
        self.frontier_states.remove(node.state)
        return node


class QueueFrontier(Frontier):
    """
    Frontier for Breadth-First Search (FIFO).
    """
    def remove(self):
        return self.remove_front()

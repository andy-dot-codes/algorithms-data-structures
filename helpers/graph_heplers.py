"""
A set of functions used throughout all other algorithms and data structures.
"""

"""
This dict is used to refer to matrix elements sourounding the current node.
"""
offsets = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}


def get_path(predecessors, start, goal):
    """
    This function goes through a list of predecessors (e.g. generated by DFS)
    and returns the path that led to fiding the goal.
    """
    current = goal
    path = []

    while current != start:
        path.append(current)
        current = predecessors[current]

    path.append(start)
    path.reverse()

    return path
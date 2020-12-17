from aoc_utils import get_input, get_input_no_line
import sys
import time
import collections
import itertools
import copy
import numpy as np

def get_neighbors(cell):
    neighbours = []
    for diff in itertools.product([-1, 0, 1], repeat=len(cell)):
        if not all(v == 0 for v in diff):
            neighbours.append(tuple(map(sum, zip(cell, diff))))
    return neighbours

def one(input):
    """
    >>> one(['.#.','..#','###'])
    112
    """
    cells = collections.defaultdict(int)
    for cell in list(itertools.product(range(-1, len(input[0]) + 1), repeat=3)):
        cells[cell] = 0

    for x, x_val in enumerate(input):
        for y, y_val in enumerate(x_val):
            if y_val == '#':
                cells[(x,y,0)] = 1
            else:
                cells[(x,y,0)] = 0
    
    for _ in range(6):
        to_change = {}
        current_state = cells.copy()
        for cell, active in current_state.items():
            neighbor_active = 0
            for neighbor in get_neighbors(cell):
                neighbor_active += cells[neighbor]
            if active and neighbor_active not in (2, 3):
                to_change[cell] = 0
            elif not active and neighbor_active == 3:
                to_change[cell] = 1

        for k, v in to_change.items():
            cells[k] = v
 
    return sum(cells.values())


def two(input):
    """
    >>> two(['.#.','..#','###'])
    848
    """
    cells = collections.defaultdict(int)
    for cell in list(itertools.product(range(-1, len(input[0]) + 1), repeat=4)):
        cells[cell] = 0

    for x, x_val in enumerate(input):
        for y, y_val in enumerate(x_val):
            if y_val == '#':
                cells[(x,y,0,0)] = 1
            else:
                cells[(x,y,0,0)] = 0
    
    for _ in range(6):
        to_change = {}
        current_state = cells.copy()
        for cell, active in current_state.items():
            neighbor_active = 0
            for neighbor in get_neighbors(cell):
                neighbor_active += cells[neighbor]
            if active and neighbor_active not in (2, 3):
                to_change[cell] = 0
            elif not active and neighbor_active == 3:
                to_change[cell] = 1

        for k, v in to_change.items():
            cells[k] = v
 
    return sum(cells.values())


def main():
    input = get_input(day=17)
    
    start = time.time()
    print("first:", one(input))
    print('It took', time.time() - start, 'seconds for first.')
    
    start = time.time()
    print("second:", two(input))
    print('It took', time.time() - start, 'seconds for second.')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        import doctest
        doctest.testmod()
    else:
        main()
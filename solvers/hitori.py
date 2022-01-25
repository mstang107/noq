from .claspy import *
from . import utils
from .utils.shading import *

def encode(string):
    return utils.encode(string)

def solve(E):
    set_max_val(max(E.R, E.C))
    s = RectangularGridShadingSolver(E.R, E.C)

    # Alone-ness in rows
    for r in range(E.R):
        number_to_coords = {}
        for c in range(E.C):
            num = E.clues[(r,c)]
            if num in number_to_coords:
                number_to_coords[num].add((r,c))
            else:
                number_to_coords[num] = {(r,c)}
        for num in number_to_coords:
            require(at_most(1, [~s.grid[y][x] for (y,x) in number_to_coords[num]]))
    # Alone-ness in cols
    for c in range(E.C):
        number_to_coords = {}
        for r in range(E.R):
            num = E.clues[(r,c)]
            if num in number_to_coords:
                number_to_coords[num].add((r,c))
            else:
                number_to_coords[num] = {(r,c)}
        for num in number_to_coords:
            require(at_most(1, [~s.grid[y][x] for (y,x) in number_to_coords[num]]))
    
    s.no_adjacent()
    s.white_connectivity()
    
    return s.solutions()


def decode(solutions):
    return utils.decode(solutions)
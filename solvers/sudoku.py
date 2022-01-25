from .claspy import *
from . import utils
from .utils.solutions import *

def encode(string):
    return utils.encode(string, has_params=True)
    
def solve(E):
    def require_1_thru_n(arr):
        for i in range(1,n+1):
            require(at_least(1, [x==i for x in arr]))

    n = E.R
    set_max_val(n)

    grid = [[IntVar(1,n) for c in range(n)] for r in range(n)]

    # ENFORCE GIVENS ARE SATISFIED
    for (i,j) in E.clues:
        require(grid[i][j] == E.clues[(i,j)])

    # ENFORCE ROWS, COLS ARE 1-n
    for i in range(n):
        require_1_thru_n([grid[i][j] for j in range(n)])
        require_1_thru_n([grid[j][i] for j in range(n)])

    # ENFORCE BOXES ARE 1-n
    m = int(n**0.5)
    for a in range(m):
        for b in range(m):
            require_1_thru_n([grid[m*a+i][m*b+j] for i in range(m) for j in range(m)])

    if E.params['Diagonal']: # ENFORCE DIAGONALS ARE 1-n
        require_1_thru_n([grid[i][i] for i in range(n)])
        require_1_thru_n([grid[i][8-i] for i in range(n)])

    if E.params['Untouch']: # ENFORCE UNTOUCH RULE
        for i in range(n-1):
            for j in range(n-1):
                require(grid[i][j] != grid[i+1][j+1])
                require(grid[i][j+1] != grid[i+1][j])

    if E.params['Antiknight']: # ENFORCE ANTIKNIGHT RULE
        for i in range(n):
            for j in range(n):
                for (di,dj) in (2,-1), (1,-2), (-1,-2), (-2,-1):
                    i0, j0 = i+di, j+dj
                    if 0 <= i0 < n and 0 <= j0 < n:
                        require(grid[i][j] != grid[i0][j0])

    # antidiagonal, nonconsecutive
    # thermo, arrow, killer, consecutive-pairs [lambda in general]
    # add possibilities for a cell
    # and then don't forget to add instructions / explanation to the controls string

    return get_all_grid_solutions(grid)

def decode(solutions):
    return utils.decode(solutions)

from .claspy import *
from . import utils
from .utils.borders import *
from .utils.loops import *
from .utils.numbers import *
from .utils.regions import *
from .utils.shading import *
from .utils.solutions import *

def encode(string):
    return utils.encode(string, outside_clues = '1111', clue_encoder = lambda x : x)

def solve(E):
    DIRECTED_CROSSES = ['+>v', '+>^', '+<v', '+<^']
    LEFT_IN = ['J^', '7v', '->'] + ['+>v', '+>^']
    RIGHT_IN = ['L^', 'rv', '-<'] + ['+<v', '+<^']
    TOP_IN = ['J<', 'L>', '1v'] + ['+<v', '+>v']
    BOTTOM_IN = ['7<', 'r>', '1^'] + ['+>^', '+<^']
    LEFT_OUT = ['J<', '7<', '-<'] + ['+<v', '+<^']
    RIGHT_OUT = ['L>', 'r>', '->'] + ['+>v', '+>^']
    TOP_OUT = ['J^', 'L^', '1^'] + ['+>^', '+<^']
    BOTTOM_OUT = ['7v', 'rv', '1v'] + ['+<v', '+>v']
    DIRECTED = ['J^', 'J<', '7v', '7<', 'L^', 'L>', 'r>', 'rv', '->', '-<', '1^', '1v', '']
    DIRECTED_STRAIGHTS = ['->', '-<', '1^', '1v', '']

    set_max_val(len(DIRECTED))

    grid = [[MultiVar(*(DIRECTED+DIRECTED_CROSSES)) for c in range(E.C)] for r in range(E.R)]

    # Entry / exit
    for c, d in E.top.items():
        if 'd' in d:
            require(var_in(grid[0][c], TOP_IN))
    for c, d in E.bottom.items():
        if 'u' in d:
            require(var_in(grid[E.R-1][c], BOTTOM_IN))
    for r, d in E.left.items():
        if 'r' in d:
            require(var_in(grid[r][0], LEFT_IN))
    for r, d in E.right.items():
        if 'l' in d:
            require(var_in(grid[r][E.C-1], RIGHT_IN))

    # Clues:
    for ((r, c), d) in E.clues.items():
        if 'l' in d:
            require(var_in(grid[r][c], LEFT_OUT))
            if 0 < c-1:
                require(var_in(grid[r][c-1], RIGHT_IN))
        if 'd' in d:
            require(var_in(grid[r][c], BOTTOM_OUT))
            if r+1 < E.R:
                require(var_in(grid[r+1][c], TOP_IN))
        if 'r' in d:
            require(var_in(grid[r][c], RIGHT_OUT))
            if c+1 < E.C:
                require(var_in(grid[r][c+1], LEFT_IN))
        if 'u' in d:
            require(var_in(grid[r][c], TOP_OUT))
            if 0 < r:
                require(var_in(grid[r-1][c], BOTTOM_IN))
        if 'i' in d:
            require(var_in(grid[r][c], DIRECTED_STRAIGHTS+DIRECTED_CROSSES+['']))

    for r in range(E.R):
        for c in range(E.C):
            if (r, c) not in E.clues or ('i' not in E.clues[(r, c)]):
                require(~var_in(grid[r][c], DIRECTED_CROSSES))

    in_reqs = []
    out_reqs = []
    loop_graph = [[Atom() for c in range(E.C)] for r in range(E.R)]

    for r in range(E.R):
        for c in range(E.C):
            if r == 0:
                in_reqs.append(var_in(grid[r][c], TOP_IN))
                out_reqs.append(var_in(grid[r][c], TOP_OUT))
                loop_graph[r][c].prove_if(var_in(grid[r][c], TOP_IN))
                loop_graph[r][c].prove_if(var_in(grid[r][c], TOP_OUT))
            elif r == E.R-1:
                in_reqs.append(var_in(grid[r][c], BOTTOM_IN))
                out_reqs.append(var_in(grid[r][c], BOTTOM_OUT))
                loop_graph[r][c].prove_if(var_in(grid[r][c], BOTTOM_IN))
                loop_graph[r][c].prove_if(var_in(grid[r][c], BOTTOM_OUT))
            if c == 0:
                in_reqs.append(var_in(grid[r][c], LEFT_IN))
                out_reqs.append(var_in(grid[r][c], LEFT_OUT))
                loop_graph[r][c].prove_if(var_in(grid[r][c], LEFT_IN))
                loop_graph[r][c].prove_if(var_in(grid[r][c], LEFT_OUT))
            elif c == E.C-1:
                in_reqs.append(var_in(grid[r][c], RIGHT_IN))
                out_reqs.append(var_in(grid[r][c], RIGHT_OUT))
                loop_graph[r][c].prove_if(var_in(grid[r][c], RIGHT_IN))
                loop_graph[r][c].prove_if(var_in(grid[r][c], RIGHT_OUT))

    require(sum_bools(1, in_reqs))
    require(sum_bools(1, out_reqs))

    def full_bfs():
        '''
        Returns:
            a set of frozensets, where each frozenset contains the (r, c)
                coordinates of an entire room
        '''
        # initially, all cells are unexplored
        unexplored_cells = set()
        for (r, c), d in E.clues.items():
            if d == 'i':
                unexplored_cells.add((r, c))

        # build a set of rooms
        # (if there are clues, we need this for stranded-edge checks)
        room_set = set()

        # --- HELPER METHOD FOR full_bfs---
        def bfs(start_cell):
            # keep track of which cells are in this connected component
            connected_component = {start_cell}

            # the start cell has now been explored
            unexplored_cells.remove(start_cell)

            # bfs!
            frontier = {start_cell}
            while frontier:
                new_frontier = set()
                for (r,c) in frontier:
                    # for each neighbor that is a valid grid cell and not in this
                    # connected component:
                    for neighbor in get_neighbors(E.R, E.C, r, c):
                        if neighbor in unexplored_cells:
                            connected_component.add(neighbor)
                            unexplored_cells.remove(neighbor)
                            new_frontier.add(neighbor)
                frontier = new_frontier
            return frozenset(connected_component)

        while len(unexplored_cells) != 0:
            # get a random start cell
            iterator = iter(unexplored_cells)
            start_cell = next(iterator)
            # run bfs on that connected component
            room = bfs(start_cell)
            # add the room to the room-set
            room_set.add(room)

        return room_set

    for ice_region in full_bfs():
        require(at_least(1, [grid[r][c] != '' for (r, c) in ice_region]))

    for r in range(E.R):
        for c in range(E.C):
            # not leftmost
            if 0 <= c-1:
                # if not leftmost and not topmost
                if 0 <= r-1:
                    if (r, c) not in E.clues or E.clues[(r,c)] != 'i':
                        # Can't only do J cases because crosses also exist
                        require((var_in(grid[r][c-1], RIGHT_IN) &
                                    var_in(grid[r-1][c], BOTTOM_OUT)) ==
                                (var_in(grid[r][c], LEFT_OUT) & var_in(grid[r][c], TOP_IN)))
                        require((var_in(grid[r][c-1], RIGHT_OUT) &
                                    var_in(grid[r-1][c], BOTTOM_IN)) ==
                                (var_in(grid[r][c], LEFT_IN) & var_in(grid[r][c], TOP_OUT)))

                        # cell is connected to loop if it's a "loop start" or
                        # if its in neighbor is part of the loop
                        if 0 <= r-2:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == 'J<') & cond(var_in(grid[r-1][c], DIRECTED_CROSSES), loop_graph[r-2][c], loop_graph[r-1][c])))
                        else:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == 'J<') & (loop_graph[r-1][c])))
                        if 0 <= c-2:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == 'J^') & cond(var_in(grid[r][c-1], DIRECTED_CROSSES), loop_graph[r][c-2], loop_graph[r][c-1])))
                        else:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == 'J^') & (loop_graph[r][c-1])))

                # if not leftmost and not bottommost
                if r+1 < E.R:
                    if (r, c) not in E.clues or E.clues[(r,c)] != 'i':
                        require((var_in(grid[r][c-1], RIGHT_IN) &
                                var_in(grid[r+1][c], TOP_OUT)) ==
                                (var_in(grid[r][c], LEFT_OUT) & var_in(grid[r][c], BOTTOM_IN)))
                        require((var_in(grid[r][c-1], RIGHT_OUT) &
                                var_in(grid[r+1][c], TOP_IN)) ==
                                (var_in(grid[r][c], LEFT_IN) & var_in(grid[r][c], BOTTOM_OUT)))
                        # cell is connected to loop if it's a "loop start" or
                        # if its in neighbor is part of the loop
                        if r+2 < E.R:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == '7<') & cond(var_in(grid[r+1][c], DIRECTED_CROSSES), loop_graph[r+2][c], loop_graph[r+1][c])))
                        else:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == '7<') & (loop_graph[r+1][c])))
                        if 0 <= c-2:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == '7v') & cond(var_in(grid[r][c-1], DIRECTED_CROSSES), loop_graph[r][c-2], loop_graph[r][c-1])))
                        else:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == '7v') & (loop_graph[r][c-1])))

                # if not leftmost and not rightmost
                if c+1 < E.C:
                    # a cell looks like a directed -, pointing left, iff:
                    #  - its left neighbor has flow in from the right
                    #  - its right neighbor has flow left
                    require((var_in(grid[r][c-1], RIGHT_IN) &
                            var_in(grid[r][c+1], LEFT_OUT)) ==
                            (var_in(grid[r][c], LEFT_OUT) & var_in(grid[r][c], RIGHT_IN)))
                    # a cell looks like a directed -, pointing right, iff:
                    #  - its left neighbor has flow right
                    #  - its right neighbor has flow in the left
                    require((var_in(grid[r][c-1], RIGHT_OUT) &
                            var_in(grid[r][c+1], LEFT_IN)) ==
                            (var_in(grid[r][c], LEFT_IN) & var_in(grid[r][c], RIGHT_OUT)))
                    # cell is connected to loop if it's a "loop start" or
                    # if its in neighbor is part of the loop
                    if c+2 < E.C:
                        loop_graph[r][c].prove_if(
                            (((grid[r][c] == '-<') | (grid[r][c] == '+<v') | (grid[r][c] == '+<^')) & cond(var_in(grid[r][c+1], DIRECTED_CROSSES), loop_graph[r][c+2], loop_graph[r][c+1])))
                    else:
                        loop_graph[r][c].prove_if(
                            (((grid[r][c] == '-<') | (grid[r][c] == '+<v') | (grid[r][c] == '+<^')) & loop_graph[r][c+1]))
                    if 0 <= c-2:
                        loop_graph[r][c].prove_if(
                            (((grid[r][c] == '->') | (grid[r][c] == '+>v') | (grid[r][c] == '+>^')) & cond(var_in(grid[r][c-1], DIRECTED_CROSSES), loop_graph[r][c-2], loop_graph[r][c-1])))
                    else:
                        loop_graph[r][c].prove_if(
                            (((grid[r][c] == '->') | (grid[r][c] == '+>v') | (grid[r][c] == '+>^')) & loop_graph[r][c-1]))

            # not rightmost
            if c+1 < E.C:
                # if not rightmost and not topmost
                if 0 <= r-1:
                    if (r, c) not in E.clues or E.clues[(r,c)] != 'i':
                        # We can't only do L cases because crosses also exist
                        require((var_in(grid[r-1][c], BOTTOM_IN) &
                                var_in(grid[r][c+1], LEFT_OUT)) ==
                                (var_in(grid[r][c], TOP_OUT) & var_in(grid[r][c], RIGHT_IN)))
                        require((var_in(grid[r-1][c], BOTTOM_OUT) &
                                var_in(grid[r][c+1], LEFT_IN)) ==
                                (var_in(grid[r][c], TOP_IN) & var_in(grid[r][c], RIGHT_OUT)))
                        # cell is connected to loop if it's a "loop start" or
                        # if its in neighbor is part of the loop
                        if c+2 < E.C:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == 'L^') & cond(var_in(grid[r][c+1], DIRECTED_CROSSES), loop_graph[r][c+2], loop_graph[r][c+1])))
                        else:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == 'L^') & (loop_graph[r][c+1])))

                        if 0 <= r-2:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == 'L>') & cond(var_in(grid[r-1][c], DIRECTED_CROSSES), loop_graph[r-2][c], loop_graph[r-1][c])))
                        else:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == 'L>') & (loop_graph[r-1][c])))

                # if not rightmost and not bottommost
                if r+1 < E.R:
                    if (r, c) not in E.clues or E.clues[(r,c)] != 'i':
                        require((var_in(grid[r][c+1], LEFT_IN) &
                                var_in(grid[r+1][c], TOP_OUT)) ==
                                (var_in(grid[r][c], RIGHT_OUT) & var_in(grid[r][c], BOTTOM_IN)))
                        require((var_in(grid[r][c+1], LEFT_OUT) &
                                var_in(grid[r+1][c], TOP_IN)) ==
                                (var_in(grid[r][c], RIGHT_IN) & var_in(grid[r][c], BOTTOM_OUT)))
                        # cell is connected to loop if it's a "loop start" or
                        # if its in neighbor is part of the loop
                        if r+2 < E.R:
                            loop_graph[r][c].prove_if(
                                (grid[r][c] == 'r>') & cond(var_in(grid[r+1][c], DIRECTED_CROSSES), loop_graph[r+2][c], loop_graph[r+1][c]))
                        else:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == 'r>') & (loop_graph[r+1][c])))
                        if c+2 < E.C:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == 'rv') & cond(var_in(grid[r][c+1], DIRECTED_CROSSES), loop_graph[r][c+2], loop_graph[r][c+1])))
                        else:
                            loop_graph[r][c].prove_if(
                                ((grid[r][c] == 'rv') & (loop_graph[r][c+1])))

            # not topmost or bottommost
            if 0 < r and r+1 < E.R:
                require((var_in(grid[r-1][c], BOTTOM_IN) &
                        var_in(grid[r+1][c], TOP_OUT)) ==
                        (var_in(grid[r][c], TOP_OUT) & var_in(grid[r][c], BOTTOM_IN)))
                require((var_in(grid[r-1][c], BOTTOM_OUT) &
                        var_in(grid[r+1][c], TOP_IN)) ==
                        (var_in(grid[r][c], TOP_IN) & var_in(grid[r][c], BOTTOM_OUT)))
                # cell is connected to loop if it's a "loop start" or
                # if its in neighbor is part of the loop
                if r+2 < E.C:
                    loop_graph[r][c].prove_if(
                        (((grid[r][c] == '1^') | (grid[r][c] == '+>^') | (grid[r][c] == '+<^')) & cond(var_in(grid[r+1][c], DIRECTED_CROSSES), loop_graph[r+2][c], loop_graph[r+1][c])))
                else:
                    loop_graph[r][c].prove_if(
                        (((grid[r][c] == '1^') | (grid[r][c] == '+>^') | (grid[r][c] == '+<^')) & loop_graph[r+1][c]))
                if 0 <= r-2:
                    loop_graph[r][c].prove_if(
                        (((grid[r][c] == '1v') | (grid[r][c] == '+<v') | (grid[r][c] == '+>v')) & cond(var_in(grid[r-1][c], DIRECTED_CROSSES), loop_graph[r-2][c], loop_graph[r-1][c])))
                else:
                    loop_graph[r][c].prove_if(
                        (((grid[r][c] == '1v') | (grid[r][c] == '+<v') | (grid[r][c] == '+>v')) & loop_graph[r-1][c]))

            if r+1 < E.R:
                require(var_in(grid[r][c], BOTTOM_OUT) == var_in(grid[r+1][c], TOP_IN))
            if 0 <= r-1:
                require(var_in(grid[r][c], TOP_OUT) == var_in(grid[r-1][c], BOTTOM_IN))
            if c+1 < E.C:
                require(var_in(grid[r][c], RIGHT_OUT) == var_in(grid[r][c+1], LEFT_IN))
            if 0 <= c-1:
                require(var_in(grid[r][c], LEFT_OUT) == var_in(grid[r][c-1], RIGHT_IN))

            # handle crosses
            require(((c-1 < 0 or (var_in(grid[r][c-1], RIGHT_IN))) &
                    ((c+1 > E.C-1) or (var_in(grid[r][c+1], LEFT_OUT)))) |
                ~((grid[r][c] == '+<v') | (grid[r][c] == '+<^')))
            require(((c-1 < 0) or (var_in(grid[r][c-1], RIGHT_OUT))) &
                    ((c+1 > E.C-1) or (var_in(grid[r][c+1], LEFT_IN))) |
                    ~((grid[r][c] == '+>v') | (grid[r][c] == '+>^')))
            require((((r-1 < 0) or (var_in(grid[r-1][c], BOTTOM_IN))) &
                    ((r+1 > E.R-1) or (var_in(grid[r+1][c], TOP_OUT)))) |
                    ~((grid[r][c] == '+<^') | (grid[r][c] == '+>^')))
            require((((r-1 < 0) or (var_in(grid[r-1][c], BOTTOM_OUT)))) &
                    ((r+1 > E.R-1) or (var_in(grid[r+1][c], TOP_IN))) |
                    ~((grid[r][c] == '+<v') | (grid[r][c] == '+>v')))

            # all non-clue, non-shaded cells are part of a loop
            require((loop_graph[r][c]) != (var_in(grid[r][c], ISOLATED)))

    def format(r, c):
        if grid[r][c].value() == '.':
            return ''
        elif grid[r][c].value() == '':
            return ''
        elif grid[r][c].value()[0] == '+':
            return '+.png'
        else:
            return DIRECTIONAL_PAIR_TO_UNICODE[grid[r][c].value()] + '.png'

    return get_all_grid_solutions(grid, format_function=format)

def decode(solutions):
    return utils.decode(solutions)

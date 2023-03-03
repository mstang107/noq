from .claspy import *
from . import utils
from .utils.loops import *

def encode(string):
    return utils.encode(string, has_borders = True, clue_encoder = lambda x : int(x) if x.isnumeric() else x)
    
def solve(E):
    if not ('s' in E.clues.values() and 'g' in E.clues.values()):
        raise ValueError('S and G squares must be provided.')

    # The largest IntVar we need is 1+(the largest clue value).
    set_max_val(max(filter(lambda x: type(x) == int, E.clues.values()))+1)

    rooms = utils.regions.full_bfs(E.R, E.C, E.edges)

    room_has_start = {room: False for room in rooms}
    room_to_number_clues = {room: set() for room in rooms}
    for room in rooms:
        for (r, c) in room:
            if type(E.clues.get((r,c))) == int:
                room_to_number_clues[room].add((r,c))
            elif E.clues.get((r,c)) == 's':
                room_has_start[room] = True

    cell_to_room, room_spanners, cell_to_out_of_region_neighbors = {}, {}, {(r,c): set() for c in range(E.C) for r in range(E.R)}
    for room in rooms:
        for (r, c) in room:
            cell_to_room[(r, c)] = room
            for (y, x) in utils.grids.get_neighbors(E.R, E.C, r, c):
                if (y, x) not in room:
                    if room not in room_spanners:
                        room_spanners[room] = set()
                    room_spanners[room].add(((r, c), (y, x)))
                    cell_to_out_of_region_neighbors[(r,c)].add((y,x))

    ALL = ['J^', 'J<', '7v', '7<', 'L^', 'L>', 'r>', 'rv', '->', '-<', '1^', '1v', 's', 'g']

    # Paths
    conn_patterns = [[MultiVar(*ALL) for c in range(E.C)] for r in range(E.R)]

    # Atoms to keep track of connectivity for each individual clue
    conn_atoms = [[Atom() for c in range(E.C)] for r in range(E.R)]

    # True at (r,c) iff the path transition onto (r,c) crosses a border.
    # boundary = [[BoolVar() for c in range(E.C)] for r in range(E.R)]
    parent = [[MultiVar('^', 'v', '<', '>', '.') for c in range(E.C)] for r in range(E.R)]

    # --- Path rules ---
    for r in range(E.R):
        for c in range(E.C):
            # --- Top / bottom edge rules ---
            if r == 0:
                require(~var_in(conn_patterns[r][c], TOP_IN+TOP_OUT))
            if r == E.R - 1:
                require(~var_in(conn_patterns[r][c], BOTTOM_IN+BOTTOM_OUT))
            # --- Left / right edge rules ---
            if c == 0:
                require(~var_in(conn_patterns[r][c], LEFT_IN+LEFT_OUT))
            if c == E.C - 1:
                require(~var_in(conn_patterns[r][c], RIGHT_IN+RIGHT_OUT))
            # --- Other connectivity rules ---
            if 0 < r:
                # Cover cases where this cell has flow in from the top.
                # Cases where top cell has flow in from the bottom will be covered in the r < E.R - 1 section.
                
                # Basic rules (no dangling edges)
                require(var_in(conn_patterns[r][c], TOP_IN+['g']) |
                    ~var_in(conn_patterns[r-1][c], BOTTOM_OUT)
                )
                # Parent tracking & connectivity
                flow_from_top = (var_in(conn_patterns[r-1][c], BOTTOM_OUT) |
                    ((conn_patterns[r-1][c] == 's') & var_in(conn_patterns[r][c], TOP_IN)))
                require(flow_from_top == (parent[r][c] == '^'))
                conn_atoms[r][c].prove_if(conn_atoms[r-1][c] & flow_from_top)

            if r < E.R - 1:
                # Cases where this cell has flow in from the bottom.

                # Basic rules (no dangling edges)
                require(var_in(conn_patterns[r][c], BOTTOM_IN+['g']) |
                    ~var_in(conn_patterns[r+1][c], TOP_OUT)
                )
                # Parent tracking
                flow_from_bottom = (var_in(conn_patterns[r+1][c], TOP_OUT) |
                    ((conn_patterns[r+1][c] == 's') & var_in(conn_patterns[r][c], BOTTOM_IN)))
                require(flow_from_bottom == (parent[r][c] == 'v'))
                conn_atoms[r][c].prove_if(conn_atoms[r+1][c] & flow_from_bottom)

            if 0 < c:
                # Cases where this cell has flow in from the left.

                # Basic rules (no dangling edges)
                require(var_in(conn_patterns[r][c], LEFT_IN+['g']) |
                    ~var_in(conn_patterns[r][c-1], RIGHT_OUT)
                )
                # Parent tracking
                flow_from_left = (var_in(conn_patterns[r][c-1], RIGHT_OUT) |
                    ((conn_patterns[r][c-1] == 's') & var_in(conn_patterns[r][c], LEFT_IN)))
                require(flow_from_left == (parent[r][c] == '<'))
                conn_atoms[r][c].prove_if(conn_atoms[r][c-1] & flow_from_left)
                
            if c < E.C - 1:
                # Cases where this cell has flow in from the right.

                # Basic rules (no dangling edges)
                require(var_in(conn_patterns[r][c], RIGHT_IN+['g']) |
                    ~var_in(conn_patterns[r][c+1], LEFT_OUT)
                )
                # Parent tracking
                flow_from_right = (var_in(conn_patterns[r][c+1], LEFT_OUT) |
                    ((conn_patterns[r][c+1] == 's') & var_in(conn_patterns[r][c], RIGHT_IN)))
                require(flow_from_right == (parent[r][c] == '>'))
                conn_atoms[r][c].prove_if(conn_atoms[r][c+1] & flow_from_right)

            conn_atoms[r][c].prove_if(E.clues.get((r,c)) == 's')
            require(conn_atoms[r][c])
    # -- Clue rules --
    for r in range(E.R):
        for c in range(E.C):
            require((conn_patterns[r][c] == 's') == (E.clues.get((r,c)) == 's'))
            require((parent[r][c] == '.') == (E.clues.get((r,c)) == 's'))
            require((conn_patterns[r][c] == 'g') == (E.clues.get((r,c)) == 'g'))

    # --- Haisu rules ---
    for room in rooms:
        if room_to_number_clues[room]:
            max_clue = max(E.clues[(r,c)] for (r,c) in room_to_number_clues[room])
            entrance_count = [[IntVar(0, max_clue+1) for c in range(E.C)] for r in range(E.R)]
            for r in range(E.R):
                for c in range(E.C):
                    require((E.clues.get((r,c)) != 's') | (entrance_count[r][c] == 0))
                    if 0 < r:
                        if (r, c) in room and (r-1, c) in cell_to_out_of_region_neighbors[(r,c)]:
                            require((parent[r][c] != '^') | (entrance_count[r][c] == cond(entrance_count[r-1][c] == max_clue+1, max_clue+1, entrance_count[r-1][c] + 1)))
                        else:
                            require((parent[r][c] != '^') | (entrance_count[r][c] == entrance_count[r-1][c]))
                    if r < E.R-1:
                        if (r, c) in room and (r+1, c) in cell_to_out_of_region_neighbors[(r,c)]:
                            require((parent[r][c] != 'v') | (entrance_count[r][c] == cond(entrance_count[r+1][c] == max_clue+1, max_clue+1, entrance_count[r+1][c] + 1)))
                        else:
                            require((parent[r][c] != 'v') | (entrance_count[r][c] == entrance_count[r+1][c]))
                    if 0 < c:
                        if (r, c) in room and (r, c-1) in cell_to_out_of_region_neighbors[(r,c)]:
                            require((parent[r][c] != '<') | (entrance_count[r][c] == cond(entrance_count[r][c-1] == max_clue+1, max_clue+1, entrance_count[r][c-1] + 1)))
                        else:
                            require((parent[r][c] != '<') | (entrance_count[r][c] == entrance_count[r][c-1]))
                    if c < E.C-1:
                        if (r, c) in room and (r, c+1) in cell_to_out_of_region_neighbors[(r,c)]:
                            require((parent[r][c] != '>') | (entrance_count[r][c] == cond(entrance_count[r][c+1] == max_clue+1, max_clue+1, entrance_count[r][c+1] + 1)))
                        else:
                            require((parent[r][c] != '>') | (entrance_count[r][c] == entrance_count[r][c+1]))
            for (r, c) in room_to_number_clues[room]:
                value = E.clues[(r,c)]
                require((entrance_count[r][c] + (1 if room_has_start[room] else 0)) == value)
        
    def format_function(r, c):
        value = E.clues.get((r,c))
        if type(value) == str and value in 'sg':
            return ''
        return f'{DIRECTIONAL_PAIR_TO_UNICODE[conn_patterns[r][c].value()]}.png'

    res = utils.solutions.get_all_grid_solutions(conn_patterns, format_function=format_function)
    return res

def decode(solutions):
    return utils.decode(solutions)
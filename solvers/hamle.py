from .claspy import *
from . import utils
from .utils.shading import *

encode, decode = utils.encode, utils.decode

def solve(E):
    # possible_values: cell -> list of possible clues that could end up at this cell
    # (each clue is identified by its coordinate pair)
    possible_values = {}
    for (clue, val) in E.clues.items():
        r, c = clue
        for new_loc in [(r+val, c), (r-val, c), (r, c-val), (r, c+val)]:
            if is_valid_coord(E.r, E.c, *new_loc):
                possible_values[new_loc] = possible_values.get(new_loc, []) + [clue]

    # grid: cell -> ID of clue that is moved there, or None
    grid = RectangularGrid(E.r, E.c, 
        lambda r, c: MultiVar(None, *possible_values.get((r,c), []))
    )

    # require that each clue gets moved to exactly one new location
    for (clue, val) in E.clues.items():
        r, c = clue

        conds = []
        for new_loc in [(r+val, c), (r-val, c), (r, c-val), (r, c+val)]:
            if is_valid_coord(E.r, E.c, *new_loc):
                conds.append(grid[new_loc] == clue)
        require(sum_bools(1, conds), clue)
    
    # convert grid to shading to check adjacency and connectivity conditions
    binary_grid = RectangularGridShadingSolver(E.r, E.c)
    for cell in grid.iter_coords():
        require(binary_grid.grid[cell] == (grid[cell] != None))
    require(binary_grid.no_adjacent())
    require(binary_grid.white_connectivity())

    return get_all_grid_solutions(
        grid,
        format_function = lambda r, c: E.clues.get(grid[(r,c)].value(), "white")
    )

# from .claspy import *
# from . import utils
# from .utils.shading import *
# from .utils.grids import *
# from .utils.solutions import *

# def encode(string):
#     return utils.encode(string)

# def solve(E):
#     # General overview of method: apply some heuristics to get a few solutions from Claspy,
#     # then perform DFS to figure out which of those solutions are real.
#     # This is to avoid using clue IDs (claspy hates IntVars).
#     set_max_val(max(4, len(E.clues)))

#     s = RectangularGridShadingSolver(E.R, E.C)
#     s.no_adjacent()

#     known_root = None
#     for ((r, c), v) in E.clues.items():
#         if v == 1:
#             known_root = (r, c)
#     s.white_connectivity(known_root)

#     # For each clue, figure out its possible destinations. Keep track of destination cells that appear more than once.
#     clue_to_possible_dests = {}
#     dest_coord_to_num_occurrences = {}
#     for ((r, c), v) in E.clues.items():
#         possible_destinations = set(filter(lambda rc: is_valid_coord(E.R, E.C, rc[0], rc[1]),
#             [(r+v, c), (r-v, c), (r, c+v), (r, c-v)]))
#         clue_to_possible_dests[(r, c)] = possible_destinations
#         for (y, x) in possible_destinations:
#             dest_coord_to_num_occurrences[(y, x)] = dest_coord_to_num_occurrences.get((y, x), 0) + 1

#     # Each clue has "unshared" possible destinations and "shared" (with other clues) possible destinations.
#     for (clue, possible_dests) in clue_to_possible_dests.items():
#         unshared_coords = frozenset(filter(lambda coord: dest_coord_to_num_occurrences[coord] == 1, possible_dests))
#         shared_coords = possible_dests.difference(unshared_coords)
#         if len(unshared_coords) > 0:
#             # At most one of the "unshared" destinations can be used.
#             require(at_most(1, [s.grid[y][x] for (y, x) in unshared_coords]))
#             # Either exactly 1 of the unshared destinations is shaded, or *at least* one of the shared destinations is shaded.
#             require(sum_bools(1, [s.grid[y][x] for (y, x) in unshared_coords]) | at_least(1, [s.grid[y][x] for (y, x) in shared_coords]))
#         else:
#             require(at_least(1, [s.grid[y][x] for (y, x) in shared_coords]))

#     # The number of shaded cells exactly equals the number of clues.
#     require(sum_bools(len(E.clues), [s.grid[r][c] for r in range(E.R) for c in range(E.C)]))

#     # If a cell cannot be the destination of any clue, it must be unshaded.
#     for r in range(E.R):
#         for c in range(E.C):
#             if (r, c) not in dest_coord_to_num_occurrences:
#                 require(~s.grid[r][c])

#     # Generate solutions
#     def dfs(clue_to_dest_coord):
#         def calculate_pairs_of_clues_to_possible_dests():
#             '''
#             For each clue, figure out which destination cells are still possible for it.
#             '''
#             clue_possible_dest_pairs = []
#             for ((r, c), v) in E.clues.items():
#                 if (r, c) in clue_to_dest_coord:
#                     continue
#                 possible_dests = tuple(filter(
#                     lambda rc: is_valid_coord(E.R, E.C, rc[0], rc[1]) and s.grid[rc[0]][rc[1]].value() and rc not in clue_to_dest_coord.values(),
#                     [(r+v, c), (r-v, c), (r, c+v), (r, c-v)]
#                 ))
#                 if len(possible_dests) > 0:
#                     clue_possible_dest_pairs.append(((r, c), possible_dests))
#                 else:
#                     return []
#             return clue_possible_dest_pairs

#         def process_single_assignments():
#             '''
#             Process clue cells which only have 1 remaining possible destination.
#             '''
#             num_assignments_made = 0
#             clue_possible_dest_pairs = calculate_pairs_of_clues_to_possible_dests()
#             clue_possible_dest_pairs.sort(key = lambda x: x[1])
#             for ((r, c), possible_dests) in clue_possible_dest_pairs:
#                 if len(possible_dests) > 1:
#                     break
#                 clue_to_dest_coord[(r, c)] = possible_dests[0]
#                 num_assignments_made += 1
#             return num_assignments_made

#         # Process single assignments a bunch of times
#         while process_single_assignments() > 0:
#             pass

#         # If we found matches for all clues, we're done.
#         if len(clue_to_dest_coord) == len(E.clues):
#             return clue_to_dest_coord
        
#         # Otherwise, make a new assignment and DFS.
#         clue_possible_dest_pairs = calculate_pairs_of_clues_to_possible_dests()
#         for ((r, c), possible_destinations) in clue_possible_dest_pairs:
#             for possible_destination in possible_destinations:
#                 new_clue_to_dest_coord = clue_to_dest_coord.copy()
#                 new_clue_to_dest_coord[(r, c)] = possible_destination
#                 sub_dfs_result = dfs(new_clue_to_dest_coord)
#                 if sub_dfs_result:
#                     return sub_dfs_result
#         return None

#     def reverse_map(m):
#         '''
#         Takes a dict-or-null, m, and returns the "reverse mapping" of m if m is a perfect bijection and None otherwise.
#         '''
#         if not m:
#             return None
#         res = {v: k for (k, v) in m.items()}
#         if len(res) == len(m):
#             return res
#         return None
    
#     solutions = []
#     for i in range(MAX_SOLUTIONS_TO_FIND):
#         if claspy_solve():
#             shaded_cells_to_clues = reverse_map(dfs({}))
#             if shaded_cells_to_clues: # If we can't actually map the shaded cells to the clues,
#             # that means our heuristics were a little off, so we won't report it as a true solution.
#                 def format_function(r, c):
#                     if (r, c) in shaded_cells_to_clues:
#                         if shaded_cells_to_clues[(r, c)] in E.clues:
#                             return E.clues[shaded_cells_to_clues[(r, c)]]
#                         else:
#                             return 'black' if s.grid[r][c].value() else 'white'
#                     return 'black' if s.grid[r][c].value() else 'white'

#                 solutions.append(get_grid_solution(s.grid, format_function = format_function))
#             avoid_duplicate_grid_solution(s.grid) # Remember to make a note of the fake solution we found before claspy_solve()!
#         else:
#             break

#     return solutions

# def decode(solutions):
#     return utils.decode(solutions)

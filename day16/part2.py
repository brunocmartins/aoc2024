from collections import deque

from utils.input_reader import read_puzzle_input
from utils.utils import timing

def find_best_route(puzzle_input):
    start, end = (), ()
    for idx_r, row in enumerate(puzzle_input):
        for idx_c, col in enumerate(row):
            if col == "S":
                start = (idx_r, idx_c)
            if col == "E":
                end = (idx_r, idx_c)
    
    len_r = len(puzzle_input)
    len_c = len(puzzle_input[0])

    rpos, cpos = start
    init_grid = [list(row) for row in puzzle_input]
    init_grid[rpos][cpos] = "O"
    seen = {(start, ">"): 0}
    # (row, column, points, direction)
    queue = deque([(rpos, cpos, 0, ">")])
    grids = deque([init_grid])

    pp = 9999999
    end_grids = []
    while queue:
        r, c, points, dir = queue.popleft()
        grid = grids.popleft()

        if (r, c) == end:
            # print(points)
            # for row in grid:
            #     print("".join(row))
            if points < pp:
                end_grids = [(points, grid)]
                pp = points
            elif points == pp:
                end_grids.append((points, grid))            
            continue

        for rr, cc, ndir in [(r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">")]:           
            if 0 <= rr < len_r and 0 <= cc < len_c and puzzle_input[rr][cc] in [".", "E"]:
                if (rr, cc, ndir) in seen and points > seen[(rr, cc, ndir)]:
                    continue

                temp_grid = [row[:] for row in grid]
                cur_points = points + 1 if dir == ndir else points + 1001
                queue.append((rr, cc, cur_points, ndir))
                temp_grid[rr][cc] = "O"
                grids.append([list(row) for row in temp_grid])
                seen[(rr, cc, ndir)] = cur_points

    seats = set()
    for _, grid in end_grids:
        for idxr, row in enumerate(grid):
            # print("".join(row))
            for idxc, col in enumerate(row):
                if col == "O":
                    seats.add((idxr, idxc))

    # for r, c in seats:
    #     init_grid[r][c] = "O"

    # for row in init_grid:
    #     print("".join(row))

    return len(seats)

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        print(find_best_route(puzzle_input))

if __name__ == "__main__":
    main()

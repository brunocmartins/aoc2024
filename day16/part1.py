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
    all_points = []
    seen = {start: 0}
    # (row, column, points, direction)
    queue = deque([(rpos, cpos, 0, ">")])
    grids = deque([init_grid])
    while queue:
        r, c, points, dir = queue.popleft()
        grid = grids.popleft()

        if (r, c) == end:
            # print("Found")
            # for row in grid:
            #     print("".join(row))
            all_points.append(points)
            continue

        for rr, cc, ndir in [(r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">")]:           
            if 0 <= rr < len_r and 0 <= cc < len_c and puzzle_input[rr][cc] in [".", "E"]:
                
                if (rr, cc) in seen and points > seen[(rr, cc)]:
                    continue
                
                cur_points = points + 1 if dir == ndir else points + 1001
                queue.append((rr, cc, cur_points, ndir))
                grid[rr][cc] = ndir
                grids.append([list(row) for row in grid])
                seen[(rr, cc)] = cur_points

    return min(all_points)

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        print(find_best_route(puzzle_input))

if __name__ == "__main__":
    main()

from collections import deque, defaultdict

from utils.input_reader import read_puzzle_input
from utils.utils import timing


def get_route(start, end, grid):
    r, c = start
    route = [start]
    queue = deque([(r, c)])

    while queue:
        r, c = queue.popleft()
        if (r, c) == end:
            route.append((r, c))
            break

        for rr, cc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if grid[rr][cc] in [".", "E"] and (rr, cc) not in route:
                route.append((rr, cc))
                queue.append((rr, cc))

    return route

def find_best_route(puzzle_input):
    start, end = (), ()
    for idx_r, row in enumerate(puzzle_input):
        for idx_c, col in enumerate(row):
            if col == "S":
                start = (idx_r, idx_c)
            if col == "E":
                end = (idx_r, idx_c)

    grid = [list(row) for row in puzzle_input]

    route = get_route(start, end, grid)
    cheats = defaultdict(set)

    for idx, (r, c) in enumerate(route):
        remaining_route = route[idx + 1:]
        for rr, cc in remaining_route:
            delta_r = rr - r
            delta_c = cc - c
            mid_pos = (r + delta_r // 2, c + delta_c // 2)

            if ((abs(delta_r) == 0 and abs(delta_c) == 2) or \
                (abs(delta_r) == 2 and abs(delta_c) == 0)) and \
                grid[mid_pos[0]][mid_pos[1]] == "#":
                cut_length = route.index((rr, cc)) - idx - 2
                cheats[cut_length].add(((r, c), mid_pos))

    cheat_options = 0
    for cut_length, positions in cheats.items():
        if cut_length >= 100:
            cheat_options += len(positions)

    return cheat_options

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        print(find_best_route(puzzle_input))

if __name__ == "__main__":
    main()

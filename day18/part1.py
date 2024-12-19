from collections import deque
import sys

from utils.input_reader import read_puzzle_input
from utils.utils import timing


def parse_input(puzzle_input):
    return [tuple(map(int, line.split(","))) for line in puzzle_input]

def get_away(puzzle_input):
    if len(sys.argv) > 1:
        width, height = 7, 7
        bt = 12
    else:
        width, height = 71, 71
        bt = 1024


    init_grid = [["." for _ in range(width)] for _ in range(height)]
    init_grid[0][0] = 0

    for (c,r) in puzzle_input[:bt]:
        init_grid[r][c] = "#"
    grids = deque([init_grid])
    step = 1
    steps = deque([step])
    init_pos = (0, 0)
    queue = deque([init_pos])
    seen = set()

    while queue and step < len(puzzle_input):
        r, c = queue.popleft()
        grid = grids.popleft()
        step = steps.popleft()

        for rr, cc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            temp_grid = [row[:] for row in grid]
            if (rr, cc) in seen:
                continue
            if 0 <= rr < height and 0 <= cc < width and temp_grid[rr][cc] == ".":
                queue.append((rr, cc))
                temp_grid[rr][cc] = "O"
                grids.append(temp_grid)
                steps.append(step + 1)
                seen.add((rr, cc))
        
                if (rr, cc) == (height - 1, width - 1):
                    # for row in temp_grid:
                    #     print("".join(map(str, row)))
                    queue.clear()
                    break

    # for idx, (c,r) in enumerate(puzzle_input):
    #     print(idx)
    #     init_grid[r][c] = "#"
    #     for row in init_grid:
    #         print("".join(map(str, row)))


    return step


def main():
    with timing():
        puzzle_input = read_puzzle_input()
        parsed_input = parse_input(puzzle_input)
        print(get_away(parsed_input))

if __name__ == "__main__":
    main()

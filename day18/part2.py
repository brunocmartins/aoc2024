from collections import deque
import sys

from utils.input_reader import read_puzzle_input
from utils.utils import timing


def parse_input(puzzle_input):
    return [tuple(map(int, line.split(","))) for line in puzzle_input]

def get_away(puzzle_input):
    if len(sys.argv) > 1:
        width, height = 7, 7
    else:
        width, height = 71, 71

    last_path = []
    for idx, (c, r) in enumerate(puzzle_input):
        if (last_path and (c,r) not in last_path) or idx < 1024: # from part 1 we know there is an exit at 1024
            continue

        init_grid = [["." for _ in range(width)] for _ in range(height)]
        init_grid[0][0] = "O"
        for (c,r) in puzzle_input[:idx+1]:
            init_grid[r][c] = "#"
        grids = deque([init_grid])
        step = 1
        steps = deque([step])
        init_pos = (0, 0)
        queue = deque([init_pos])
        seen = set()

        found = False

        while queue:
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
                        # print("Found for idx: ", idx)
                        found = True
                        last_path = []
                        for i in range(height):
                            for j in range(width):
                                if temp_grid[i][j] == "O":
                                    last_path.append((j,i))

                        queue.clear()
                        break

        if not found:
            break
    return puzzle_input[idx]
        # for idx, (c,r) in enumerate(puzzle_input):
        #     print(idx)
        #     init_grid[r][c] = "#"
        #     for row in init_grid:
        #         print("".join(map(str, row)))


    # return step


def main():
    with timing():
        puzzle_input = read_puzzle_input()
        parsed_input = parse_input(puzzle_input)
        print(get_away(parsed_input))

if __name__ == "__main__":
    main()

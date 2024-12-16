import re
import sys

from utils.input_reader import read_puzzle_input
from utils.utils import timing


def parse_input(puzzle_input):
    parsed_input = {}
    for idx, line in enumerate(puzzle_input):
        pattern = r"[pv]=(-?\d+),(-?\d+)"
        matches = re.findall(pattern, line)
        parsed_input[idx] = [(int(x), int(y)) for x, y in matches]

    return parsed_input


def get_positions(puzzle_input):
    if len(sys.argv) > 1:
        width, height = 11, 7
    else:
        width, height = 101, 103

    seen = []
    seconds = 0
    while True:
        grid = [[0 for _ in range(width)] for _ in range(height)]
        for pos, vel in puzzle_input.values():
            x, y = pos
            vx, vy = vel

            final_x = (x + seconds * vx) % width
            final_y = (y + seconds * vy) % height

            grid[final_y][final_x] = 1

        print(f"Seconds: {seconds}")
        for row in grid:
            print("".join(["#" if x == 1 else " " for x in row]))
        print("\n\n")

        if grid in seen:
            break
        else:
            seen.append(grid)
            seconds += 1


def main():
    with timing():
        puzzle_input = read_puzzle_input()
        parsed_input = parse_input(puzzle_input)
        print(get_positions(parsed_input))

if __name__ == "__main__":
    main()

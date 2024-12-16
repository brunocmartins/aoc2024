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

    seconds = 100

    quad_1, quad_2, quad_3, quad_4 = [], [], [], []
    for pos, vel in puzzle_input.values():
        x, y = pos
        vx, vy = vel

        final_x = (x + seconds * vx) % width
        final_y = (y + seconds * vy) % height

        if final_x < width//2 and final_y < height//2:
            quad_1.append((final_x, final_y))
        elif final_x > width//2 and final_y < height//2:
            quad_2.append((final_x, final_y))
        elif final_x < width//2 and final_y > height//2:
            quad_3.append((final_x, final_y))
        elif final_x > width//2 and final_y > height//2:
            quad_4.append((final_x, final_y))

    return (len(quad_1) * len(quad_2) * len(quad_3) * len(quad_4))

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        parsed_input = parse_input(puzzle_input)
        print(get_positions(parsed_input))

if __name__ == "__main__":
    main()

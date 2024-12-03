import re

from utils.input_reader import read_puzzle_input
from day03.part1 import get_result


def concat_lines(puzzle_input):
    return ["".join(puzzle_input)]

def get_matches(puzzle_input):
    pattern = r"mul\((\d+),\s*(\d+)\)"
    matches = []

    for line in puzzle_input:
        dos = [m.span() for m in re.finditer(r"do\(\)", line)]
        donts = [m.span() for m in re.finditer(r"don't\(\)", line)]

        if donts[0] < dos[0]:
            matches += re.findall(pattern, line[:donts[0][0]])

        dont_idx = 0
        for do in dos:
            if do[0] > donts[dont_idx][1]:
                for idx, dont in enumerate(donts):
                    if do[1] < dont[0]:
                        matches += re.findall(pattern, line[do[0]:dont[0]])
                        dont_idx = idx
                        break
                    elif do[1] > donts[-1][1]:
                        matches += re.findall(pattern, line[do[0]:])
                        break

    return matches

def main():
    puzzle_input = read_puzzle_input(3)
    concat_puzzle_input = concat_lines(puzzle_input)
    matches = get_matches(concat_puzzle_input)
    print(get_result(matches))

if __name__ == "__main__":
    main()

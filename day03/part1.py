import re

from utils.input_reader import read_puzzle_input


def get_matches(puzzle_input):
    matches = []
    pattern = r"mul\((\d+),\s*(\d+)\)"
    for line in puzzle_input:
        matches += re.findall(pattern, line)
    return matches

def get_result(matches):
    return sum([int(n1) * int(n2) for n1, n2 in matches])

def main():
    puzzle_input = read_puzzle_input(3)
    
    matches = get_matches(puzzle_input)
    print(get_result(matches))

if __name__ == "__main__":
    main()

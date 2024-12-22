from collections import deque

from utils.input_reader import read_puzzle_input
from utils.utils import timing


def parse_input(puzzle_input):
    available_towels = [towel for row in puzzle_input[:puzzle_input.index("")] for towel in row.split(", ")]
    patterns = puzzle_input[puzzle_input.index("") + 1:]
    
    return available_towels, patterns

def get_possible_patterns(available_towels, patterns):
    possible_patterns = set()

    for pattern in patterns:
        offsets = deque([0])
        seen = []

        while offsets:
            offset = offsets.popleft()
            if offset == len(pattern):
                possible_patterns.add(pattern)
            for towel in available_towels:
                if towel in pattern[offset:offset + len(towel)]:
                    towel_offset = pattern.index(towel, offset) + len(towel)
                    if towel_offset not in seen:
                        offsets.append(towel_offset)
                        seen.append(towel_offset)



    return len(possible_patterns)

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        available_towels, patterns = parse_input(puzzle_input)
        print(get_possible_patterns(available_towels, patterns))

if __name__ == "__main__":
    main()

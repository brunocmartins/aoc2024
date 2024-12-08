from collections import defaultdict

from utils.input_reader import read_puzzle_input
from day08.part1 import get_antenna_positions


def get_antinodes(puzzle_input, antenna_positions):
    rr = len(puzzle_input)
    cc = len(puzzle_input[0])

    antinodes = set()

    for antenna, positions in antenna_positions.items():
        # print(positions)
        for i in range(len(positions)):
            pos = positions[:i] + positions[i+1:]
            # print(pos)
            for r, c in pos:
                dr = positions[i][0] - r
                dc = positions[i][1] - c
                for j in range(1, max(rr, cc)):
                    antinode = (positions[i][0] + j * dr, positions[i][1] + j * dc)
                    if 0 <= antinode[0] < rr and 0 <= antinode[1] < cc:
                        antinodes.add(antinode)
                    else:
                        break

            if len(positions) > 1:
                antinodes.add(positions[i])
        
    return antinodes

def main():
    puzzle_input = read_puzzle_input()
    antenna_positions = get_antenna_positions(puzzle_input)
    print(len(get_antinodes(puzzle_input, antenna_positions)))

if __name__ == "__main__":
    main()

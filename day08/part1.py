from collections import defaultdict

from utils.input_reader import read_puzzle_input


def get_antenna_positions(puzzle_input):
    antenna_positions = defaultdict(list)
    for r_idx, line in enumerate(puzzle_input):
        for c_idx, char in enumerate(line):
            if char.isalnum():
                antenna_positions[char].append((r_idx, c_idx))

    return antenna_positions

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
                antinode = (positions[i][0] + dr, positions[i][1] + dc)
                # print(dr, dc)
                if 0 <= antinode[0] < rr and 0 <= antinode[1] < cc:
                    antinodes.add(antinode)
        
    return antinodes

def main():
    puzzle_input = read_puzzle_input()
    antenna_positions = get_antenna_positions(puzzle_input)
    print(len(get_antinodes(puzzle_input, antenna_positions)))

if __name__ == "__main__":
    main()

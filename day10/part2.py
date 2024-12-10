from utils.input_reader import read_puzzle_input


MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def get_hiking(puzzle_input):
    hikes = 0

    for row, line in enumerate(puzzle_input):
        for col, char in enumerate(line):
            if char == "0":
                trail = True
                element = int(char)
                positions = [(row, col)]
                found_positions = []
                while trail:
                    for dir, move in MOVES.items():
                        for position in positions:
                            test_position = (position[0] + move[0], position[1] + move[1])

                            if 0 <= test_position[0] < len(puzzle_input) and 0 <= test_position[1] < len(puzzle_input[0]):
                                if int(puzzle_input[test_position[0]][test_position[1]]) == element + 1:
                                    found_positions.append(test_position)
                    if element == 9:
                        trail = False
                        hikes += len(positions)
                    elif len(found_positions) == 0:
                        trail = False
                        
                    else:
                        element += 1

                    positions = found_positions
                    found_positions = []
    
    return hikes


def main():
    puzzle_input = read_puzzle_input()
    print(get_hiking(puzzle_input))

if __name__ == "__main__":
    main()

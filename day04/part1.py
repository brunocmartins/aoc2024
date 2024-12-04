from utils.input_reader import read_puzzle_input


def _count_xmas(line_list):
    word_search = "XMAS"
    matches = 0
    for line in line_list:
        for idx, char in enumerate(line):
            if line[idx:idx+len(word_search)] == word_search:
                matches += 1
            elif line[idx:idx+len(word_search)] == word_search[::-1]:
                matches += 1

    return matches

def _get_diagonals(input_list, direction):
    diagonals = {}

    for r_idx, row in enumerate(input_list):
        for c_idx, col in enumerate(row):
            diagonal_key = r_idx + c_idx if direction == "left" else r_idx - c_idx
            if diagonal_key not in diagonals:
                diagonals[diagonal_key] = []
            diagonals[diagonal_key].append(col)

    return ["".join(diagonals[key]) for key in sorted(diagonals.keys())]


def get_matches(puzzle_input):
    word_search = "XMAS"
    matches = 0

    horizontal_lines = puzzle_input
    vertical_lines = ["".join(item) for item in zip(*puzzle_input)]
    left_diagonals = _get_diagonals(puzzle_input, "left")
    right_diagonals = _get_diagonals(puzzle_input, "right")

    all_lines = horizontal_lines + vertical_lines + left_diagonals + right_diagonals

    return _count_xmas(all_lines)


def main():
    puzzle_input = read_puzzle_input(4, sample=False)
    print(get_matches(puzzle_input))


if __name__ == "__main__":
    main()

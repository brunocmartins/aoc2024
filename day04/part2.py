from utils.input_reader import read_puzzle_input


def _has_xmas(line):
    word_search = "MAS"
    for idx, char in enumerate(line):
        if line[idx:idx+len(word_search)] == word_search:
            return True
        elif line[idx:idx+len(word_search)] == word_search[::-1]:
            return True

    return False

def _get_diagonals(input_list, direction):
    diagonals = {}

    for r_idx, row in enumerate(input_list):
        for c_idx, col in enumerate(row):
            diagonal_key = r_idx + c_idx if direction == "left" else r_idx - c_idx
            if diagonal_key not in diagonals:
                diagonals[diagonal_key] = []
            diagonals[diagonal_key].append(col)

    print(diagonals)

    return ["".join(diagonals[key]) for key in sorted(diagonals.keys())]


def get_matches(puzzle_input):
    word_search = "MAS"
    matches = 0
    match_list = []
    for r_idx, row in enumerate(puzzle_input):
        for c_idx, char in enumerate(row):
            if char in ["S", "M"]:
                for i in range(len(word_search)):
                    try:
                        x = puzzle_input[r_idx][c_idx] + puzzle_input[r_idx + 1][c_idx + 1] + puzzle_input[r_idx + 2][c_idx + 2]
                    except IndexError:
                        x = ""

                    if _has_xmas(x):
                        rev_x = puzzle_input[r_idx][c_idx+2] + puzzle_input[r_idx + 1][c_idx + 1] + puzzle_input[r_idx+2][c_idx]
                        if _has_xmas(rev_x):
                            matches +=1
                            match_list.append([x, rev_x])
                            break

    print(match_list)

    return matches


def main():
    puzzle_input = read_puzzle_input(4, sample=False)
    print(get_matches(puzzle_input))


if __name__ == "__main__":
    main()

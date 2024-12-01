from utils.input_reader import read_puzzle_input


def get_entry_list(puzzle_input) -> list:
    left_list, right_list = [], []

    for line in puzzle_input:
        left, right = list(filter(None, line.strip().split(" ")))
        left_list.append(left)
        right_list.append(right)

    assert len(left_list) == len(right_list)

    return sorted(left_list), sorted(right_list)

def get_distances(left_list: list, right_list: list) -> list:
    distances = []
    for i in range(len(left_list)):
        left, right = left_list[i], right_list[i]
        distances.append(abs(int(right) - int(left)))

    return distances

def main():
    puzzle_input = read_puzzle_input(1)
    left, right = get_entry_list(puzzle_input)
    print(sum(get_distances(left, right)))

if __name__ == "__main__":
    main()

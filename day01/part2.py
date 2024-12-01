from utils.input_reader import read_puzzle_input
from day01.part1 import get_entry_list


def get_similarity_score(left_list: list, right_list: list) -> list:
    similarity_scores = []
    for i in range(len(left_list)):
        _count = right_list.count(left_list[i])
        similarity_scores.append(int(left_list[i]) * _count)

    return similarity_scores

def main():
    puzzle_input = read_puzzle_input(1)
    left, right = get_entry_list(puzzle_input)
    print(sum(get_similarity_score(left, right)))

if __name__ == "__main__":
    main()

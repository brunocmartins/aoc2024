from utils.input_reader import read_puzzle_input
from utils.utils import timing


def parse_input(puzzle_input):
    nums = []
    for line in puzzle_input:
        nums.extend(line.split())

    return nums

def next_iter(num_str):
    if num_str == "0":
        return ["1"]
    elif len(num_str) % 2 == 0:
        half_len = len(num_str) // 2
        left = num_str[:half_len].lstrip("0")
        right = num_str[half_len:].lstrip("0")

        if not left:
            left = "0"
        if not right:
            right = "0"

        return [left, right]
    else:
        val = int(num_str)
        val *= 2024
        return [str(val)]

def count_after_iterations(num_str, steps, memo):
    if steps == 0:
        return 1

    key = (num_str, steps)
    if key in memo:
        return memo[key]

    next_nums = next_iter(num_str)

    total_count = 0
    for n in next_nums:
        print(n)
        total_count += count_after_iterations(n, steps - 1, memo)
        print(next_nums, total_count)

    memo[key] = total_count
    return total_count

def get_arrangement(puzzle_input):
    memory = {}
    total = 0

    for gem_num in puzzle_input:
        total += count_after_iterations(gem_num, 2, memory)
        
    return total

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        parsed_input = parse_input(puzzle_input)
        print(get_arrangement(parsed_input))

if __name__ == "__main__":
    main()

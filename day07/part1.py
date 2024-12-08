import itertools

from utils.input_reader import read_puzzle_input


def parse_input(puzzle_input):
    parsed_input = {}
    for line in puzzle_input:
        results, nums = line.split(": ")
        numbers = list(map(int, [nums.strip() for nums in nums.split(" ")]))
        parsed_input[int(results)] = numbers

    return parsed_input

def get_valid_equations(puzzle_input):
    sums = 0

    for line in puzzle_input:
        part = line.split()
        result = int(part[0][:-1])
        nums = list(map(int, part[1:]))

        op_combinations = itertools.product("+*", repeat=len(nums) - 1)

        for op_combination in op_combinations:
            equation = int(nums[0])
            for idx, op in enumerate(op_combination):
                equation = eval(f"{equation} {op} {nums[idx+1]}")

            if equation == result:
                sums += result
                break
        
    return sums


def main():
    puzzle_input = read_puzzle_input()
    print(get_valid_equations(puzzle_input))

if __name__ == "__main__":
    main()

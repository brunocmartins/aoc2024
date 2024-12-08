import itertools

from utils.input_reader import read_puzzle_input


def get_valid_equations(puzzle_input):
    sums = 0

    for line in puzzle_input:
        part = line.split()
        result = int(part[0][:-1])
        nums = list(map(int, part[1:]))

        operators = ["+", "*", "||"]
        op_combinations = itertools.product(operators, repeat=len(nums) - 1)

        for op_combination in op_combinations:
            equation = int(nums[0])
            for idx, op in enumerate(op_combination):
                if op == "||":
                    equation = eval(f"{equation}{nums[idx+1]}")
                else:
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

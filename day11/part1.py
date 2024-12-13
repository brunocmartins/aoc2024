from utils.input_reader import read_puzzle_input
from utils.utils import timing


def parse_input(puzzle_input):
    for line in puzzle_input:
        nums = line.split()

    return [int(num) for num in nums]

def get_arrangement(puzzle_input):
    iterations = 0
    gem_numbers = puzzle_input
    while iterations < 25:
        new_iteration = []
        for gem_number in gem_numbers:

            if gem_number == 0:
                new_iteration.append(1)
            elif len(str(gem_number)) % 2 == 0:
                g1 = int(str(gem_number)[:len(str(gem_number))//2])
                g2 = int(str(gem_number)[len(str(gem_number))//2:])
                new_iteration.extend([g1, g2])
            else:
                new_iteration.append(gem_number * 2024)

        gem_numbers = new_iteration
        iterations += 1
        
    return len(gem_numbers)

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        parsed_input = parse_input(puzzle_input)
        print(get_arrangement(parsed_input))

if __name__ == "__main__":
    main()

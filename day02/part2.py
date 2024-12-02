from utils.input_reader import read_puzzle_input
from day02.part1 import parse_input, _is_safe


def parse_report(report):
    safe_levels = []
    for level in report:
        if _is_safe(level):
            safe_levels.append(level)
        else:
            for idx in range(len(level)):
                adjusted_level = level[:idx] + level[idx+1:]
                if _is_safe(adjusted_level):
                    safe_levels.append(adjusted_level)
                    break


    return safe_levels
            

def main():
    puzzle_input = read_puzzle_input(2, sample=False)
    parsed_input = parse_input(puzzle_input)
    print(len(parse_report(parsed_input)))


if __name__ == "__main__":
    main()

from utils.input_reader import read_puzzle_input


def parse_input(puzzle_input):
    return [line.split() for line in puzzle_input]

def _is_safe(report):
    sig = 1 if int(report[1]) > int(report[0]) else -1
    for n1, n2 in zip(report, report[1:]):
        delta = sig * (int(n2) - int(n1))
        if not (1 <= delta <= 3):
            return False
        
    else:
        return True

def parse_report(report):
    safe_levels = []
    for level in report:
        if _is_safe(level):
            safe_levels.append(level)

    return safe_levels
            

def main():
    puzzle_input = read_puzzle_input(2)
    parsed_input = parse_input(puzzle_input)
    print(len(parse_report(parsed_input)))


if __name__ == "__main__":
    main()

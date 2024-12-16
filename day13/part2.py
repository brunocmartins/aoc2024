import re
import sys
from collections import defaultdict

from utils.utils import timing

def parse_input():
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = "input"

    with open(f"day13/{filename}.txt") as file:
        data = file.read().split("\n\n")

    puzzle_input = defaultdict(list)
    for idx, buttons in enumerate(data):
        pattern = r"Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)"
        matches = re.findall(pattern, buttons)[0]
        for i in range(0, len(matches), 2):
            x, y = matches[i], matches[i+1]
            puzzle_input[idx].append((int(x), int(y)))

    return puzzle_input

def try_values(but_a, but_b, prize):
    actual_prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)


    j = (but_a[0]*actual_prize[1] - but_a[1]*actual_prize[0])/(but_a[0]*but_b[1] - but_a[1]*but_b[0])
    i = (actual_prize[0] - but_b[0]*j)/but_a[0]
    
    if i.is_integer() and j.is_integer() and i >= 0 and j >= 0:
        return [(int(i), int(j))]


def get_fewest_tokens(puzzle_input):
    weigth_a = 3
    weigth_b = 1

    tokens = 0
    for buttons in puzzle_input.values():
        but_a, but_b, prize = buttons[0], buttons[1], buttons[2]
        valid_games = try_values(but_a, but_b, prize)

        if valid_games:
            tokens += min([weigth_a*game[0] + weigth_b*game[1] for game in valid_games])
        
    return tokens


def main():
    with timing():
        puzzle_input = parse_input()
        print(get_fewest_tokens(puzzle_input))

if __name__ == "__main__":
    main()

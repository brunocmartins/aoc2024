from utils.input_reader import read_puzzle_input
from utils.utils import timing


def mix(x, y):
    return x ^ y

def prune(x):
    return x % 16777216

def get_secret(puzzle_input):
    number_2000th = 0
    for sn in map(int, puzzle_input):
        for i in range(2000):
            sn = prune(mix(sn, sn * 64))
            sn = prune(mix(sn, sn // 32))
            sn = prune(mix(sn, sn * 2048))

            if i == 1999:
                number_2000th += sn

    return number_2000th

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        print(get_secret(puzzle_input))

if __name__ == '__main__':
    main()

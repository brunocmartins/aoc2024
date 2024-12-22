from collections import defaultdict

from utils.input_reader import read_puzzle_input
from utils.utils import timing


def mix(x, y):
    return x ^ y

def prune(x):
    return x % 16777216

def get_secret(puzzle_input):
    sequences = defaultdict(list)
    for sn in map(int, puzzle_input):
        buyer_sequence = {}
        prices = []
        for i in range(2000):
            sn = prune(mix(sn, sn * 64))
            sn = prune(mix(sn, sn // 32))
            sn = prune(mix(sn, sn * 2048))

            price = int(str(sn)[-1])
            prices.append(price)
            if i > 3:
                deltas = [x - y for x, y in zip(prices[i-3:i+1], prices[i-4:i])]
                if tuple(deltas) not in buyer_sequence:
                    buyer_sequence[tuple(deltas)] = price

        for sequence, price in buyer_sequence.items():
            sequences[sequence].append(price)

    max_bananas = (0, ())
    for sequence, prices in sequences.items():
        total_price = sum(prices)
        if total_price > max_bananas[0]:
            max_bananas = (total_price, sequence)

    return max_bananas

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        print(get_secret(puzzle_input))

if __name__ == '__main__':
    main()

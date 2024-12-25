from collections import defaultdict
import sys

from utils.utils import timing


def read_input():
    infile = f"day25/{sys.argv[1]}.txt" if len(sys.argv)>=2 else 'day25/input.txt'
    input = open(infile).read().strip().split('\n\n')

    locks, keys = [], []
    for schematic in input:
        if schematic.startswith("#####"):
            locks.append(convert_to_height(schematic.split("\n")))
        elif schematic.startswith("....."):
            keys.append(convert_to_height(schematic.split("\n")))
        else:
            raise ValueError("Invalid input")

    return locks, keys

def convert_to_height(schematic):
    heights = [-1 for _ in range(len(schematic[0]))]
    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            if schematic[i][j] == "#":
                heights[j] += 1

    return heights

            

def get_fit(locks, keys):
    fits = 0
    for lock in locks:
        for key in keys:
            sums = [x + y for x, y in zip(lock, key)]
            if max(sums) <= len(lock):
                fits += 1

    return fits


def main():
    with timing():
        locks, keys = read_input()
        print(get_fit(locks, keys))

if __name__ == '__main__':
    main()

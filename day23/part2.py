import re
from collections import defaultdict

from utils.input_reader import read_puzzle_input
from utils.utils import timing


def get_lan_connections(puzzle_input):
    lan_connections = set()
    comp_wired = defaultdict(set)
    for line in puzzle_input:
        parts = line.split("-")
        possible = list()
        for part in parts:
            r = re.compile(f".*{part}.*")
            wired_computers = list()
            [wired_computers.extend(wire.split("-")) for wire in filter(r.match, puzzle_input)]

            for computer in wired_computers:
                if computer not in parts:
                    if computer not in possible:
                        possible.append(computer)
                    else:
                        comp_wired[part].update([*parts, computer])
                        lan_connections.add(tuple(sorted([*parts, computer])))

    biggest = 0
    chain = []
    for comp, wires in comp_wired.items():
        sum_wires = 0
        for wire in wires:
            if comp in comp_wired.get(wire, []) and len(wires) == len(comp_wired[wire]):
                sum_wires += 1
        if sum_wires == len(wires):
            if len(wires) > biggest:
                biggest = len(wires)
                chain = list(wires)

    return ",".join(sorted(chain))

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        print(get_lan_connections(puzzle_input))

if __name__ == '__main__':
    main()

import re

from utils.input_reader import read_puzzle_input
from utils.utils import timing


def get_lan_connections(puzzle_input):
    lan_connections = set()
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
                    elif any(item.startswith("t") for item in [*parts, computer]):
                        lan_connections.add(tuple(sorted([*parts, computer])))

    return len(lan_connections)

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        print(get_lan_connections(puzzle_input))

if __name__ == '__main__':
    main()

from collections import defaultdict

from utils.input_reader import read_puzzle_input
from utils.utils import timing

    
def get_sides(positions):
    up, down, left, right = set(), set(), set(), set()
    for r, c in positions:
        if (r - 1, c) not in positions:
            up.add((r, c))
        if (r + 1, c) not in positions:
            down.add((r, c))
        if (r, c - 1) not in positions:
            left.add((r, c))
        if (r, c + 1) not in positions:
            right.add((r, c))

    sides = 0
    for r, c in up:
        if (r, c) in left:
            sides += 1
        if (r, c) in right:
            sides += 1
        if (r - 1, c - 1) in right and (r, c) not in left:
            sides += 1
        if (r - 1, c + 1) in left and (r, c) not in right:
            sides += 1

    for r, c in down:
        if (r, c) in left:
            sides += 1
        if (r, c) in right:
            sides += 1
        if (r + 1, c - 1) in right and (r, c) not in left:
            sides += 1
        if (r + 1, c + 1) in left and (r, c) not in right:
            sides += 1

    return sides


def get_fence_price(puzzle_input):
    r_len = len(puzzle_input)
    c_len = len(puzzle_input[0])

    visited = [[False] * c_len for _ in range(r_len)]
    gardens = defaultdict(list)
    idx = 0

    for r in range(r_len):
        for c in range(c_len):
            if not visited[r][c]:
                idx += 1
                garden = puzzle_input[r][c]
                queue = [(r, c)]
                visited[r][c] = True
                gardens[(garden, idx)].append((r, c))

                while queue:
                    r_idx, c_idx = queue.pop()
                    for rr, cc in [(r_idx - 1, c_idx), (r_idx + 1, c_idx), (r_idx, c_idx - 1), (r_idx, c_idx + 1)]:
                        if 0 <= rr < r_len and 0 <= cc < c_len and not visited[rr][cc] and puzzle_input[rr][cc] == garden:
                            visited[rr][cc] = True
                            queue.append((rr, cc))
                            gardens[(garden, idx)].append((rr, cc))

    fence_price = 0
    for garden in gardens.values():
        area = len(garden)
        sides = get_sides(garden)
        fence_price += area * sides

    return fence_price
    

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        print(get_fence_price(puzzle_input))

if __name__ == "__main__":
    main()

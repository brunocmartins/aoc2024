from collections import defaultdict

from utils.input_reader import read_puzzle_input
from utils.utils import timing

    
def get_perimeter(positions):
    per = list()
    for pos in positions:
        r, c = pos
        if (r - 1, c) not in positions:
            per.append((r - 1, c))
        if (r + 1, c) not in positions:
            per.append((r + 1, c))
        if (r, c - 1) not in positions:
            per.append((r, c - 1))
        if (r, c + 1) not in positions:
            per.append((r, c + 1))

    return len(per)

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
        perimeter = get_perimeter(garden)
        fence_price += area * perimeter

    return fence_price
    

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        print(get_fence_price(puzzle_input))

if __name__ == "__main__":
    main()

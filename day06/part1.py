from utils.input_reader import read_puzzle_input


def parse_input(puzzle_input):
    grid = [list(row) for row in puzzle_input]
    for r_idx, row in enumerate(grid):
        for c_idx, col in enumerate(row):
            if col in "^v<>":
                return grid, (r_idx, c_idx), col

def move(pos, dir):
    r, c = pos
    if dir == "^":
        return (r - 1, c)
    elif dir == "v":
        return (r + 1, c)
    elif dir == "<":
        return (r, c - 1)
    elif dir == ">":
        return (r, c + 1)
    else:
        raise ValueError(f"Invalid direction {dir}")

def turn_right(dir):
    directions = "^>v<"
    return directions[(directions.index(dir) + 1) % 4]

def get_patrol(puzzle_input):
    grid, pos, dir = parse_input(puzzle_input)
    visited = set()
    visited.add(pos)
    in_patrol = True

    while in_patrol:
        next_pos = move(pos, dir)
        if grid[next_pos[0]][next_pos[1]] == "#":
            dir = turn_right(dir)
        else:
            pos = next_pos
            visited.add(pos)
            grid[pos[0]][pos[1]] = "X"
        
        if pos[0] in [0, len(grid) - 1] or pos[1] in [0, len(grid[0]) - 1]:
            in_patrol = False
        
    for row in grid:
        print("".join(row))
    return len(visited)

def main():
    puzzle_input = read_puzzle_input()
    print(get_patrol(puzzle_input))

if __name__ == "__main__":
    main()

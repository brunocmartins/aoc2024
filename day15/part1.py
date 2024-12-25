from utils.input_reader import read_puzzle_input
from utils.utils import timing


def parse_input(puzzle_input):
    grid = []
    for row in puzzle_input[:puzzle_input.index("")]:
        grid.append([char for char in row])
    movements = "".join(puzzle_input[puzzle_input.index("") + 1:])

    return grid, movements

def next_position(pos, dir):
    if dir == "^":
        return (pos[0] - 1, pos[1])
    elif dir == "v":
        return (pos[0] + 1, pos[1])
    elif dir == "<":
        return (pos[0], pos[1] - 1)
    elif dir == ">":
        return (pos[0], pos[1] + 1)
    
    return False


def get_next_pos(grid, pos, dir):
    next_pos = next_position(pos, dir)

    if grid[next_pos[0]][next_pos[1]] == "#":
        return grid, pos

    elif grid[next_pos[0]][next_pos[1]] == ".":
        grid[pos[0]][pos[1]] = "."
        grid[next_pos[0]][next_pos[1]] = "@"
        return grid, next_pos

    elif grid[next_pos[0]][next_pos[1]] == "O":
        nps = [] # next positions
        o_pos = next_pos
        while True:
            nps.append(next_position(o_pos, dir))
            np = nps[-1]
            if grid[np[0]][np[1]] == ".":
                grid[pos[0]][pos[1]] = "."
                grid[next_pos[0]][next_pos[1]] = "@"
                for p in nps:
                    grid[p[0]][p[1]] = "O"
                return grid, next_pos
            elif grid[np[0]][np[1]] == "#":
                return grid, pos
            elif grid[np[0]][np[1]] == "O":
                o_pos = np
            else:
                raise ValueError("Invalid character in grid")
    else:
        raise ValueError("Invalid character in grid")


def get_iterations(grid, movements):
    len_r = len(grid)
    len_c = len(grid[0])

    start_pos = None
    for i in range(len_r):
        for j in range(len_c):
            if grid[i][j] == "@":
                start_pos = (i, j)
                break
        if start_pos:
            break

    cur_pos = start_pos
    for move in movements:
        grid, cur_pos = get_next_pos(grid, cur_pos, move)

        # for row in grid:
        #     print("".join(row))

    gps_coords = 0
    for r in range(len_r):
        for c in range(len_c):
            if grid[r][c] == "O":
                gps_coords += 100 * r + c
    
    return gps_coords

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        grid, movements = parse_input(puzzle_input)
        print(get_iterations(grid, movements))

if __name__ == "__main__":
    main()

from itertools import cycle

from utils.input_reader import read_puzzle_input


def get_checksum(puzzle_input):
    disk_map = puzzle_input[0]
    rearrenged_disk_map = []
    id = 0

    for idx, num in enumerate(disk_map):
        if idx % 2 == 0:
            rearrenged_disk_map.extend([str(id)] * int(num))
            id += 1
        else:
            rearrenged_disk_map.extend(["."] * int(num))

    number_idxs = [idx for idx, val in enumerate(rearrenged_disk_map) if val.isdigit()]
    for i in range(len(list(rearrenged_disk_map))-1):
        if rearrenged_disk_map[i] == "." and i < number_idxs[-1]:
            number_idx_move = number_idxs.pop()
            rearrenged_disk_map[i], rearrenged_disk_map[number_idx_move] = rearrenged_disk_map[number_idx_move], rearrenged_disk_map[i]
    
    checksum = 0
    for idx, val in enumerate(rearrenged_disk_map):
        if val == ".":
            break
        else:
            checksum += (int(val) * (idx))

    return checksum

def main():
    puzzle_input = read_puzzle_input()
    print(get_checksum(puzzle_input))

if __name__ == "__main__":
    main()

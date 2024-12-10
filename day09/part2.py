from collections import defaultdict

from utils.input_reader import read_puzzle_input


def get_checksum(puzzle_input):
    disk_map = puzzle_input[0]
    rearrenged_disk_map = []
    id_map = {}
    id = 0
    dot_idxs = []
    overall_idx = 0
    for idx, num in enumerate(disk_map):
        if idx % 2 == 0:
            rearrenged_disk_map.extend([str(id)] * int(num))
            id_map[id] = int(num)
            overall_idx += int(num)
            id += 1
        else:
            rearrenged_disk_map.extend(["."] * int(num))
            dot_idxs.append((int(num), [oidx for oidx in range(overall_idx, overall_idx + int(num))]))
            overall_idx += int(num)

    number_idxs = defaultdict(list)
    for idx, id in enumerate(rearrenged_disk_map):
        if id.isdigit():
            number_idxs[int(id)].append(idx)


    for id in reversed(id_map.keys()):
        id_size = id_map[id]
        num_idx = number_idxs[id][0]

        for dot_idx, (dot_size, idxs) in enumerate(dot_idxs):
            if dot_size >= id_size and idxs[-1] < num_idx:
                rearrenged_disk_map[idxs[0]: idxs[0] + id_size] = rearrenged_disk_map[number_idxs[id][0]:number_idxs[id][-1] + 1]
                rearrenged_disk_map[number_idxs[id][0]:number_idxs[id][-1] + 1] = ["."] * id_size
                dot_idxs[dot_idx] = (dot_size - id_size, idxs[id_size:])
                break

    checksum = 0
    for idx, val in enumerate(rearrenged_disk_map):
        if val == ".":
            continue
        else:
            checksum += (int(val) * idx)

    return checksum

def main():
    puzzle_input = read_puzzle_input()
    print(get_checksum(puzzle_input))

if __name__ == "__main__":
    main()

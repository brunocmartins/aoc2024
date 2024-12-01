def read_puzzle_input(day_num, sample: bool = False):
    file = "sample" if sample else "input"
    with open(f"day{day_num:02d}/{file}.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines

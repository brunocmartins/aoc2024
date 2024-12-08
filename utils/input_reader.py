import inspect
import os
import sys

def read_puzzle_input():
    if len(sys.argv) > 1 and sys.argv[1] == "sample":
        file = "sample"
    else:
        file = "input"

    caller_frame = inspect.stack()[1]
    caller_path = os.path.dirname(caller_frame.filename)

    folder_name = os.path.basename(caller_path)
    day_num = "".join(filter(str.isdigit, folder_name))

    if not day_num:
        raise ValueError(f"No numeric identifier found in folder name: {folder_name}")

    with open(f"day{int(day_num):02d}/{file}.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines

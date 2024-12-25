import re

from utils.input_reader import read_puzzle_input
from utils.utils import timing


def get_combo_operand(instruction, registers):
    if 0 <= instruction <= 3:
        return instruction
    elif 4 <= instruction <= 6:
        return registers[instruction - 4]

    return -1


def parse_input(puzzle_input):
    registers = []
    for register in puzzle_input[:puzzle_input.index("")]:
        pattern = r"Register [ABC]: (\d+)"
        match = re.search(pattern, register)
        if match:
            registers.append(int(match.group(1)))

    program = puzzle_input[puzzle_input.index("") + 1:]
    instructions = list(map(int, re.findall(r"\d+", program[0])))
    
    return registers, instructions

def run_program(registers, instructions):
    out = []
    pointer = 0
    while pointer < len(instructions):
        opcode = instructions[pointer]
        operand = instructions[pointer + 1]
        combo = get_combo_operand(operand, registers)

        if opcode == 0:
            registers[0] = registers[0] // (2 ** combo)
            pointer += 2
        elif opcode == 1:
            registers[1] = registers[1] ^ operand
            pointer += 2
        elif opcode == 2:
            registers[1] = combo % 8
            pointer += 2
        elif opcode == 3:
            if registers[0] == 0:
                pointer += 2
            else:
                pointer = operand
        elif opcode == 4:
            registers[1] = registers[1] ^ registers[2]
            pointer += 2
        elif opcode == 5:
            out.append(int(combo % 8))
            pointer += 2
        elif opcode == 6:
            registers[1] = registers[0] // (2 ** combo)
            pointer += 2
        elif opcode == 7:
            registers[2] = registers[0] // (2 ** combo)
            pointer += 2

    return ",".join([str(i) for i in out])

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        registers, instructions = parse_input(puzzle_input)
        print(run_program(registers, instructions))

if __name__ == "__main__":
    main()

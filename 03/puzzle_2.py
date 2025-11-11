import re

from puzzle_1 import load_input

if __name__ == "__main__":
    lines = load_input()

    instructions = [
        match
        for line in lines
        for match in re.findall(
            r"(mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don\'t\(\)))", line
        )
    ]

    enabled = True
    total = 0
    for instruction in instructions:
        if instruction[0] == "do()":
            enabled = True

        if instruction[0] == "don't()":
            enabled = False

        if enabled and instruction[0].startswith("mul"):
            total += int(instruction[1]) * int(instruction[2])

    print(total)

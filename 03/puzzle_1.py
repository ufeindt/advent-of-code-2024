import re


def load_input() -> list[list[int]]:
    with open("03/input.txt") as f:
        lines = [line.strip() for line in f]

    return lines


if __name__ == "__main__":
    lines = load_input()

    print(
        sum(
            int(a) * int(b)
            for line in lines
            for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
        )
    )

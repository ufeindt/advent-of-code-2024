from itertools import product
from tqdm import tqdm


def load_input(filename: str = "07/input") -> list[tuple[int, list[int]]]:
    with open(filename) as f:
        lines = [
            (
                int(line.split(":")[0]),
                [int(a) for a in line.split(": ")[1].split(" ")],
            )
            for line in f
        ]

    return lines


def filter_valid(
    lines: list[tuple[int, list[int]]], operator_options: list[str] = ["+", "*"]
) -> list[tuple[int, list[int]]]:
    filter_lines = []
    for line in tqdm(lines):
        for operators in product(*[operator_options for _ in range(len(line[1]) - 1)]):
            result = line[1][0]
            for operator, number in zip(operators, line[1][1:]):
                if operator == "+":
                    result += number
                elif operator == "*":
                    result *= number
                elif operator == "||":
                    result = int(f"{result}{number}")
            if int(result) == line[0]:
                filter_lines.append(line)
                break

    return filter_lines


def main():
    test_lines = load_input(filename="07/test_input")
    assert sum(line[0] for line in filter_valid(test_lines)) == 3749

    lines = load_input()
    print(sum(line[0] for line in filter_valid(lines)))


if __name__ == "__main__":
    main()

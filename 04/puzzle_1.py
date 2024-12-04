import re


def load_input(filename: str = "04/input.txt") -> list[str]:
    with open(filename) as f:
        rows = [line.strip() for line in f.readlines()]

    n_rows = len(rows)
    n_columns = len(rows[0])
    columns = ["".join(row[k] for row in rows) for k in range(n_columns)]

    diagonals = []
    for x_start in range(0, n_columns):
        diagonal = ""
        for k, x in enumerate(range(x_start, n_columns)):
            diagonal += rows[k][x]
        diagonals.append(diagonal)

    for x_start in range(0, n_columns):
        diagonal = ""
        for k, x in enumerate(range(0, x_start + 1)):
            diagonal += rows[x_start - k][x]
        diagonals.append(diagonal)

    for y_start in range(1, n_rows):
        diagonal = ""
        for k, y in enumerate(range(y_start, n_rows)):
            diagonal += rows[y][k]
        diagonals.append(diagonal)

    for y_start in range(1, n_rows):
        diagonal = ""
        for k, y in enumerate(range(y_start, n_rows)):
            diagonal += rows[y][n_columns - k - 1]
        diagonals.append(diagonal)

    return [*rows, *columns, *diagonals]


def get_pattern_count(patterns: [str], lines: list[str]) -> int:
    return sum(
        len([match for pattern in patterns for match in re.findall(pattern, line)])
        for line in lines
    )


def main():
    patterns = [r"XMAS", r"SAMX"]
    test_input = load_input("04/test_input.txt")
    assert get_pattern_count(patterns, test_input) == 18

    input = load_input()
    print(get_pattern_count(patterns, input))


if __name__ == "__main__":
    main()

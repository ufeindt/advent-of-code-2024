def load_input(filename: str = "04/input") -> list[str]:
    with open(filename) as f:
        rows = [line.strip() for line in f.readlines()]

    n_rows = len(rows)
    n_columns = len(rows[0])

    return [
        (
            f"{rows[y-1][x-1]}{rows[y][x]}{rows[y+1][x+1]}",
            f"{rows[y-1][x+1]}{rows[y][x]}{rows[y+1][x-1]}",
        )
        for x in range(1, n_columns - 1)
        for y in range(1, n_rows - 1)
    ]


def get_pattern_count(crosses: list[tuple[str, str]]) -> int:
    return len(
        [
            cross
            for cross in crosses
            if all(line == "MAS" or line == "SAM" for line in cross)
        ]
    )


def main():
    test_input = load_input("04/test_input")
    assert get_pattern_count(test_input) == 9

    input = load_input()
    print(get_pattern_count(input))


if __name__ == "__main__":
    main()

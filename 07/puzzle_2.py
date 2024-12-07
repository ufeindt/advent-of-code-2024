from puzzle_1 import filter_valid, load_input


def main():
    test_lines = load_input(filename="07/test_input")
    assert (
        sum(
            line[0]
            for line in filter_valid(test_lines, operator_options=["+", "*", "||"])
        )
        == 11387
    )

    lines = load_input()
    print(
        sum(line[0] for line in filter_valid(lines, operator_options=["+", "*", "||"]))
    )


if __name__ == "__main__":
    main()

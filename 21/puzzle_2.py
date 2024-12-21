from puzzle_1 import get_human_keypress_count, load_input


def solve(filename: str = "21/input") -> int:
    codes = load_input(filename=filename)
    return sum(
        get_human_keypress_count(code, n_robots=26) * int(code[:-1]) for code in codes
    )


def main():
    print(solve())


if __name__ == "__main__":
    main()

from puzzle_1 import load_input, solve_maze


def solve(filename="16/input") -> int | None:
    walls, start, end = load_input(filename=filename)
    paths = solve_maze(walls, start, end)

    return len({(a_[0], a_[1]) for path in paths for a in path[0] for a_ in a})


def main():
    assert solve(filename="16/test_input") == 45
    assert solve(filename="16/second_test_input") == 64
    print(solve())


if __name__ == "__main__":
    main()

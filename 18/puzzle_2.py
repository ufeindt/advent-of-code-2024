from puzzle_1 import find_path, load_input


def solve(
    filename: str = "18/input", goal: tuple[int, int] = (70, 70), n_fallen: int = 1024
) -> tuple[int, int] | None:
    falling_bytes = load_input(filename=filename)
    path = find_path(falling_bytes, goal, n_fallen)
    n = 1
    for k in range(n_fallen + 1, len(falling_bytes)):
        if (next_byte := falling_bytes[k - 1]) in path:
            path = find_path(falling_bytes, goal, k)
            n += 1

        if not path:
            print(n)
            return next_byte


def main():
    # assert solve(filename="18/test_input", goal=(6, 6), n_fallen=12) == (6, 1)
    print(solve())


if __name__ == "__main__":
    main()

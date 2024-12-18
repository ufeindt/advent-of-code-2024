from puzzle_1 import find_path, load_input


def solve(
    filename: str = "18/input", goal: tuple[int, int] = (70, 70), n_fallen: int = 1024
) -> tuple[int, int] | None:
    falling_bytes = load_input(filename=filename)
    path = find_path(falling_bytes, goal, n_fallen)
    min_n = n_fallen + 1
    max_n = len(falling_bytes) - 1
    while max_n != min_n:
        n_fallen = (max_n + min_n) // 2
        path = find_path(falling_bytes, goal, n_fallen)

        if max_n == min_n + 1:
            if path:
                return falling_bytes[n_fallen]
            else:
                return falling_bytes[n_fallen - 1]

        if path:
            min_n = n_fallen
        else:
            max_n = n_fallen


def main():
    assert solve(filename="18/test_input", goal=(6, 6), n_fallen=12) == (6, 1)
    print(solve())


if __name__ == "__main__":
    main()

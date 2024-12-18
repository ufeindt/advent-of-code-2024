from puzzle_1 import find_path, load_input
from tqdm import tqdm


def solve(
    filename: str = "18/input", goal: tuple[int, int] = (70, 70), n_fallen: int = 1024
) -> tuple[int, int] | None:
    falling_bytes = load_input(filename=filename)
    for k in tqdm(range(n_fallen + 1, len(falling_bytes))):
        if not find_path(falling_bytes, goal, k):
            return falling_bytes[k - 1]


def main():
    # print(solve(filename="18/test_input", goal=(6, 6), n_fallen=12))
    assert solve(filename="18/test_input", goal=(6, 6), n_fallen=12) == (6, 1)
    print(solve())


if __name__ == "__main__":
    main()

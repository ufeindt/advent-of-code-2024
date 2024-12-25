import os

MODULE_DIR = os.path.dirname(__file__)


def load_input(
    filename: str = os.path.join(MODULE_DIR, "input"),
) -> tuple[list[tuple[int, int, int, int, int]], list[tuple[int, int, int, int, int]]]:
    with open(filename) as f:
        locks_and_keys = f.read().split("\n\n")

    locks = []
    keys = []
    for lock_or_key in locks_and_keys:
        columns = []
        for k1, line in enumerate(lock_or_key.split("\n")):
            if k1 == 0:
                for cell in line:
                    columns.append([cell])
            else:
                for k2, cell in enumerate(line):
                    columns[k2].append(cell)

        counts = [
            len([cell for cell in column if cell == "#"]) - 1 for column in columns
        ]
        if lock_or_key.startswith("#####"):
            locks.append(counts)
        else:
            keys.append(counts)

    return locks, keys


def check_lock_and_key(
    lock: tuple[int, int, int, int, int],
    key: tuple[int, int, int, int, int],
    max_sum: int = 5,
) -> bool:
    for lock_col, key_col in zip(lock, key, strict=True):
        if lock_col + key_col > max_sum:
            return False
    return True


def solve(filename: str = os.path.join(MODULE_DIR, "input")) -> int:
    locks, keys = load_input(filename)
    total = 0
    for lock in locks:
        for key in keys:
            if check_lock_and_key(lock, key):
                total += 1
    return total


def main():
    assert solve(filename=os.path.join(MODULE_DIR, "test_input")) == 3
    print(solve())


if __name__ == "__main__":
    main()

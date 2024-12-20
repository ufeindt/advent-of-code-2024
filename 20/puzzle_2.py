from puzzle_1 import find_cheats, find_path, load_input


def solve(
    filename: str = "20/input", min_dt: int = 100, max_dist_cheat: int = 20
) -> int | None:
    walls, start, end = load_input(filename=filename)
    path = find_path(walls, start, end)
    cheats = find_cheats(path, walls, min_dt=min_dt, max_dist_cheat=max_dist_cheat)

    return len(cheats)


def main():
    assert solve(filename="20/test_input", min_dt=76) == 3
    assert solve(filename="20/test_input", min_dt=74) == 7
    assert solve(filename="20/test_input", min_dt=72) == 29
    assert solve(filename="20/test_input", min_dt=70) == 41
    assert solve(filename="20/test_input", min_dt=68) == 55
    assert solve(filename="20/test_input", min_dt=66) == 67
    assert solve(filename="20/test_input", min_dt=64) == 86
    assert solve(filename="20/test_input", min_dt=62) == 106
    assert solve(filename="20/test_input", min_dt=60) == 129
    assert solve(filename="20/test_input", min_dt=58) == 154
    assert solve(filename="20/test_input", min_dt=56) == 193
    assert solve(filename="20/test_input", min_dt=54) == 222
    assert solve(filename="20/test_input", min_dt=52) == 253
    assert solve(filename="20/test_input", min_dt=50) == 285
    print(solve())


if __name__ == "__main__":
    main()

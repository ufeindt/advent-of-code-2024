from puzzle_1 import solve


def main():
    assert solve(filename="13/test_input") == 480
    print(solve(offset=10_000_000_000_000))


if __name__ == "__main__":
    main()

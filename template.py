import os

MODULE_DIR = os.path.dirname(__file__)


def load_input(filename: str = os.path.join(MODULE_DIR, "input")) -> None:
    with open(filename) as f:
        ...


def solve(filename: str = os.path.join(MODULE_DIR, "input")) -> int:
    data = load_input(filename)
    return -1


def main():
    assert solve(filename=os.path.join(MODULE_DIR, "test_input")) == 0
    print(solve())


if __name__ == "__main__":
    main()

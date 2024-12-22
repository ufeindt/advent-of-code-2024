import os
from functools import cache

MODULE_DIR = os.path.dirname(__file__)


def load_input(filename: str = os.path.join(MODULE_DIR, "input")) -> list[int]:
    with open(filename) as f:
        return [int(line.strip()) for line in f]


@cache
def next_secret(secret: int) -> int:
    secret ^= secret << 6
    secret %= 1 << 24
    secret ^= secret >> 5
    secret %= 1 << 24
    secret ^= secret << 11
    secret %= 1 << 24

    return secret


def solve(filename: str = os.path.join(MODULE_DIR, "input")) -> int:
    secrets = load_input(filename)
    total = 0

    for secret in secrets:
        for _ in range(2000):
            secret = next_secret(secret)

        total += secret

    return total


def main():
    assert solve(filename=os.path.join(MODULE_DIR, "test_input")) == 37327623
    print(solve())


if __name__ == "__main__":
    main()

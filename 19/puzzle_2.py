from functools import cache

from puzzle_1 import load_input


@cache
def count_all_combinations(desired_pattern: str, available: str) -> int:
    n_combinations = 0
    for available_pattern in available.split(", "):
        if available_pattern == desired_pattern:
            n_combinations += 1

        if desired_pattern.endswith(available_pattern):
            if n := count_all_combinations(
                desired_pattern[: -len(available_pattern)], available
            ):
                n_combinations += n

    return n_combinations


def solve(filename: str = "19/input") -> int:
    available, desired = load_input(filename=filename)

    return sum(
        [
            count_all_combinations(desired_pattern, available)
            for desired_pattern in desired
        ]
    )


def main():
    assert solve(filename="19/test_input") == 16
    print(solve())


if __name__ == "__main__":
    main()

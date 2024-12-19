from functools import cache


def load_input(filename: str = "19/input") -> tuple[str, list[str]]:
    with open(filename) as f:
        available = f.readline().strip()
        f.readline()
        desired = [line.strip() for line in f]

    return available, desired


@cache
def find_combination(desired_pattern: str, available: str) -> list[str] | None:
    for available_pattern in available.split(", "):
        if available_pattern == desired_pattern:
            return [available_pattern]

        if desired_pattern.startswith(available_pattern):
            if combination := find_combination(
                desired_pattern[len(available_pattern) :], available
            ):
                return [available_pattern] + combination


def solve(filename: str = "19/input") -> int:
    available, desired = load_input(filename=filename)

    return len(
        [
            desired_pattern
            for desired_pattern in desired
            if find_combination(desired_pattern, available)
        ]
    )


def main():
    assert solve(filename="19/test_input") == 6
    print(solve())


if __name__ == "__main__":
    main()

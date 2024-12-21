from functools import cache


def load_input(filename: str = "21/input") -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f]


@cache
def get_numerical_direction_options(start: str, end: str) -> set[str]:
    keys = {
        "0": (1, 3),
        "1": (0, 2),
        "2": (1, 2),
        "3": (2, 2),
        "4": (0, 1),
        "5": (1, 1),
        "6": (2, 1),
        "7": (0, 0),
        "8": (1, 0),
        "9": (2, 0),
        "A": (2, 3),
    }

    start_coords = keys[start]
    end_coords = keys[end]

    dx = end_coords[0] - start_coords[0]
    dy = end_coords[1] - start_coords[1]

    options = set()
    if (start_coords[0] + dx, start_coords[1]) in keys.values():
        options.add(
            (">" if dx > 0 else "<") * abs(dx)
            + ("v" if dy > 0 else "^") * abs(dy)
            + "A"
        )
    if (start_coords[0], start_coords[1] + dy) in keys.values():
        options.add(
            ("v" if dy > 0 else "^") * abs(dy)
            + (">" if dx > 0 else "<") * abs(dx)
            + "A"
        )

    return options


@cache
def get_directional_keypress_count(start: str, end: str, n_robots=3) -> int:
    if n_robots == 1:
        return 1
    keys = {
        "^": (1, 0),
        "v": (1, 1),
        "<": (0, 1),
        ">": (2, 1),
        "A": (2, 0),
    }

    start_coords = keys[start]
    end_coords = keys[end]

    dx = end_coords[0] - start_coords[0]
    dy = end_coords[1] - start_coords[1]
    options = set()
    if (start_coords[0] + dx, start_coords[1]) in keys.values():
        options.add(
            (">" if dx > 0 else "<") * abs(dx)
            + ("v" if dy > 0 else "^") * abs(dy)
            + "A"
        )

    if (start_coords[0], start_coords[1] + dy) in keys.values():
        options.add(
            ("v" if dy > 0 else "^") * abs(dy)
            + (">" if dx > 0 else "<") * abs(dx)
            + "A"
        )

    return min(
        sum(
            get_directional_keypress_count(start, end, n_robots=n_robots - 1)
            for start, end in zip("A" + option[:-1], option, strict=True)
        )
        for option in options
    )


def get_human_keypress_count(code: str, n_robots: int = 3):
    keypress_options = [
        get_numerical_direction_options(start, end)
        for start, end in zip("A" + code[:-1], code, strict=True)
    ]

    total = 0
    for options in keypress_options:
        total += min(
            sum(
                get_directional_keypress_count(start, end, n_robots=n_robots)
                for start, end in zip("A" + option[:-1], option, strict=True)
            )
            for option in options
        )
    return total


def solve(filename: str = "21/input") -> int:
    codes = load_input(filename=filename)
    return sum(get_human_keypress_count(code) * int(code[:-1]) for code in codes)


def main():
    assert solve(filename="21/test_input") == 126384
    print(solve())


if __name__ == "__main__":
    main()

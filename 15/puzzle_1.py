def load_input(filename: str = "15/input") -> tuple[dict[tuple[int, int], str], str]:
    with open(filename) as f:
        map_raw, instructions_raw = f.read().split("\n\n")

    map = {
        (x, y): cell
        for y, row in enumerate(map_raw.split("\n"))
        for x, cell in enumerate(row)
        if cell != "."
    }
    instructions = instructions_raw.replace("\n", "")

    return map, instructions


def move_robot(
    map: dict[tuple[int, int], str], instructions: str
) -> dict[tuple[int, int], str]:
    directions = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}

    x, y = [(x, y) for (x, y), c in map.items() if c == "@"][0]
    map.pop((x, y))

    for instruction in instructions:
        direction = directions[instruction]
        first_box = None
        x_check, y_check = x, y
        empty_space_found = False
        while not empty_space_found:
            x_check += direction[0]
            y_check += direction[1]

            if (checked_cell := map.get((x_check, y_check))) == "#":
                break
            elif checked_cell == "O" and not first_box:
                first_box = (x_check, y_check)
            elif not checked_cell:
                empty_space_found = True

        if empty_space_found:
            # print(instruction, first_box, (x_check, y_check))
            if first_box:
                map[(x_check, y_check)] = map.pop(first_box)
            x, y = x + direction[0], y + direction[1]

        # print_map(map, x, y)

    return map


def print_map(map: dict[tuple[int, int], str], x_bot: int, y_bot: int):
    max_x = max(x for (x, _) in map.keys())
    max_y = max(y for (_, y) in map.keys())

    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            if x == x_bot and y == y_bot:
                line += "@"
            elif cell := map.get((x, y)):
                line += cell
            else:
                line += "."
        print(line)
    print()


def sum_gps(map: dict[tuple[int, int], str]) -> int:
    return sum([100 * y + x for (x, y), c in map.items() if c == "O"])


def solve(filename: str = "15/input") -> int:
    map, instructions = load_input(filename=filename)
    map = move_robot(map, instructions)
    return sum_gps(map)


def main():
    assert solve(filename="15/small_test_input") == 2028
    # return
    assert solve(filename="15/test_input") == 10092
    print(solve())


if __name__ == "__main__":
    main()

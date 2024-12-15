from puzzle_1 import print_map


def load_input(filename: str = "15/input") -> tuple[dict[tuple[int, int], str], str]:
    with open(filename) as f:
        map_raw, instructions_raw = f.read().split("\n\n")

    map = {}
    for y, row in enumerate(map_raw.split("\n")):
        for x, cell in enumerate(row):
            match cell:
                case "O":
                    map[(2 * x, y)] = "["
                    map[(2 * x + 1, y)] = "]"
                case "#":
                    map[(2 * x, y)] = "#"
                    map[(2 * x + 1, y)] = "#"
                case "@":
                    map[(2 * x, y)] = "@"

    instructions = instructions_raw.replace("\n", "")

    return map, instructions


def move_robot(
    map: dict[tuple[int, int], str], instructions: str, show_map: bool = False
) -> dict[tuple[int, int], str]:
    directions = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}

    x, y = [(x, y) for (x, y), c in map.items() if c == "@"][0]
    map.pop((x, y))
    if show_map:
        print_map(map, x, y)

    for k, instruction in enumerate(instructions):
        if show_map:
            print(k, instruction, (x, y))
        direction = directions[instruction]
        boxes = set()
        to_check = {(x + direction[0], y + direction[1])}
        empty_space_found = False
        while not empty_space_found:
            if show_map:
                print(to_check)
            checked_cells = {(x_, y_): map.get((x_, y_)) for x_, y_ in to_check}
            if any(cell == "#" for cell in checked_cells.values()):
                break
            elif any(cell in ("[", "]") for cell in checked_cells.values()):
                to_check = set()
                for (x_, y_), cell in checked_cells.items():
                    if cell not in ("[", "]"):
                        continue

                    if instruction in ("<", ">"):
                        boxes |= {(x_, y_), (x_ + direction[0], y_)}
                        to_check |= {(x_ + 2 * direction[0], y_)}
                    else:
                        boxes |= {(x_, y_), (x_ + (1 if cell == "[" else -1), y_)}
                        to_check |= {
                            (x_, y_ + direction[1]),
                            (x_ + (1 if cell == "[" else -1), y_ + direction[1]),
                        }
            elif all(cell is None for cell in checked_cells.values()):
                empty_space_found = True

        if empty_space_found:
            if boxes:
                new_boxes = {
                    (x_ + direction[0], y_ + direction[1]): map.pop((x_, y_))
                    for x_, y_ in boxes
                }
                map.update(new_boxes)
            x, y = x + direction[0], y + direction[1]

        if show_map:
            print(boxes)
            print_map(map, x, y)

    return map


def sum_gps(map: dict[tuple[int, int], str]) -> int:
    return sum([100 * y + x for (x, y), c in map.items() if c == "["])


def solve(filename: str = "15/input", show_map: bool = False) -> int:
    map, instructions = load_input(filename=filename)
    map = move_robot(map, instructions, show_map=show_map)
    return sum_gps(map)


def main():
    assert solve(filename="15/test_input") == 9021
    print(solve())


if __name__ == "__main__":
    main()

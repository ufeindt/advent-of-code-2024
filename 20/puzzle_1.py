def load_input(
    filename: str = "20/input",
) -> tuple[set[tuple[int, int]], tuple[int, int], tuple[int, int]]:
    with open(filename) as f:
        lines = [line.strip() for line in f]

    start, end = None, None
    walls = set()
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            match cell:
                case "#":
                    walls.add((x, y))
                case "S":
                    start = x, y
                case "E":
                    end = x, y

    if not start or not end:
        raise ValueError("Input file missing start and/or end position.")

    return walls, start, end


def find_path(
    walls: set[tuple[int, int]],
    start: tuple[int, int],
    end: tuple[int, int],
    t_cheat: int | None = None,
) -> list[tuple[int, int]]:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    queue = [(start, [start])]
    visited = {start}
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path

        for direction in directions:
            next_coords = (current[0] + direction[0], current[1] + direction[1])
            if next_coords not in visited and (
                len(path) == t_cheat or next_coords not in walls
            ):
                visited.add(next_coords)
                queue.append((next_coords, path + [next_coords]))

    return []


def find_cheats(
    path: list[tuple[int, int]],
    walls: set[tuple[int, int]],
    min_dt: int = 100,
    max_dist_cheat: int = 2,
) -> dict[tuple[int, int, int, int], int]:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    path_dict = {coords: t for t, coords in enumerate(path)}
    cheats = {}
    for coords, t in path_dict.items():
        for main_direction in directions:
            if main_direction[0] == 0:
                secondary_directions = [(-1, 0), (1, 0)]
            else:
                secondary_directions = [(0, -1), (0, 1)]

            for secondary_direction in secondary_directions:
                possible_cheat_coords = []
                for k_main in range(1, max_dist_cheat + 1):
                    for k_secondary in range(0, max_dist_cheat - k_main + 1):
                        if (
                            cheat_coords := (
                                coords[0]
                                + k_main * main_direction[0]
                                + k_secondary * secondary_direction[0],
                                coords[1]
                                + k_main * main_direction[1]
                                + k_secondary * secondary_direction[1],
                            )
                        ) not in path_dict:
                            continue

                        possible_cheat_coords.append(cheat_coords)

                for cheat_coords in possible_cheat_coords:
                    t_cheat = path_dict[cheat_coords]
                    if (
                        dist := abs(cheat_coords[0] - coords[0])
                        + abs(cheat_coords[1] - coords[1])
                    ) > max_dist_cheat:
                        continue

                    if (dt := t_cheat - t - dist) < min_dt:
                        continue

                    cheats[(*coords, *cheat_coords)] = dt

    return cheats


def solve(filename: str = "20/input", min_dt: int = 100) -> int | None:
    walls, start, end = load_input(filename=filename)
    path = find_path(walls, start, end)
    cheats = find_cheats(path, walls, min_dt=min_dt)

    return len(cheats)


def main():
    assert solve(filename="20/test_input", min_dt=64) == 1
    assert solve(filename="20/test_input", min_dt=40) == 2
    assert solve(filename="20/test_input", min_dt=38) == 3
    assert solve(filename="20/test_input", min_dt=36) == 4
    assert solve(filename="20/test_input", min_dt=20) == 5
    assert solve(filename="20/test_input", min_dt=12) == 8
    assert solve(filename="20/test_input", min_dt=10) == 10
    assert solve(filename="20/test_input", min_dt=8) == 14
    assert solve(filename="20/test_input", min_dt=6) == 16
    assert solve(filename="20/test_input", min_dt=4) == 30
    assert solve(filename="20/test_input", min_dt=2) == 44
    print(solve())


if __name__ == "__main__":
    main()

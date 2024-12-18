from enum import Enum


class Facing(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


DIRECTIONS = {
    Facing.EAST: (1, 0),
    Facing.SOUTH: (0, 1),
    Facing.WEST: (-1, 0),
    Facing.NORTH: (0, -1),
}


def load_input(
    filename: str = "16/input",
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


def solve_maze(
    walls: set[tuple[int, int]], start: tuple[int, int], end: tuple[int, int]
) -> list[tuple[list[list[tuple[int, int, int]]], int]]:
    queue = [((start[0], start[1], Facing.EAST.value), [[]], 0)]
    visited = {queue[0][0]}
    paths = []
    while queue:
        (current, path, score) = queue.pop(0)
        if current[:2] == end:
            paths.append((path, score))
            continue

        options = [
            (
                (
                    current[0] + DIRECTIONS[Facing(current[2])][0],
                    current[1] + DIRECTIONS[Facing(current[2])][1],
                    current[2],
                ),
                score + 1,
            ),
            ((current[0], current[1], (current[2] + 1) % 4), score + 1000),
            ((current[0], current[1], (current[2] - 1) % 4), score + 1000),
        ]
        for next_coords, next_score in options:
            if next_coords[:2] in walls:
                continue
            if next_coords in visited:
                if matching_queue := [
                    k
                    for k, a in enumerate(queue)
                    if a[0] == next_coords and next_score == a[2]
                ]:
                    k = matching_queue[0]
                    queue[k][1].extend([a + [next_coords] for a in path])
                continue

            visited.add(next_coords)
            queue.append((next_coords, [a + [next_coords] for a in path], next_score))
        queue = sorted(queue, key=lambda a: a[2])

    min_score = min([a[1] for a in paths])
    best_paths = [a for a in paths if a[1] == min_score]
    return best_paths


def solve(filename: str = "16/input") -> int | None:
    walls, start, end = load_input(filename=filename)
    paths = solve_maze(walls, start, end)

    return paths[0][1]


def main():
    assert solve(filename="16/test_input") == 7036
    assert solve(filename="16/second_test_input") == 11048
    print(solve())


if __name__ == "__main__":
    main()

import re


def load_input(filename: str = "18/input") -> list[tuple[int, int]]:
    with open(filename) as f:
        input = [(int(m[0]), int(m[1])) for m in re.findall(r"(\d+),(\d+)", f.read())]

    return input


def find_path(
    falling_bytes: list[tuple[int, int]], goal: tuple[int, int], n_fallen: int
) -> int | None:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    obstacles = set(falling_bytes[:n_fallen])
    queue = [((0, 0), [])]
    visited = {(0, 0)}
    paths = []
    while queue:
        current, path = queue.pop(0)
        if current == goal:
            paths.append(path)
            continue

        for direction in directions:
            next_coords = (current[0] + direction[0], current[1] + direction[1])
            if (
                next_coords[0] >= 0
                and next_coords[0] <= goal[0]
                and next_coords[1] >= 0
                and next_coords[1] <= goal[1]
                and next_coords not in visited
                and next_coords not in obstacles
            ):
                visited.add(next_coords)
                queue.append((next_coords, path + [next_coords]))
    if not paths:
        return None

    return min([len(path) for path in paths])


def solve(
    filename: str = "18/input", goal: tuple[int, int] = (70, 70), n_fallen: int = 1024
) -> int | None:
    falling_bytes = load_input(filename=filename)
    return find_path(falling_bytes, goal, n_fallen)


def main():
    assert solve(filename="18/test_input", goal=(6, 6), n_fallen=12) == 22
    print(solve())


if __name__ == "__main__":
    main()

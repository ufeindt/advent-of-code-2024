import os
from itertools import combinations

MODULE_DIR = os.path.dirname(__file__)


def load_input(filename: str = os.path.join(MODULE_DIR, "input")) -> list[list[str]]:
    with open(filename) as f:
        return [line.strip().split("-") for line in f]


def group_connections(connection_list: list[list[str]]) -> dict[str, set[str]]:
    connections = {}
    for c1, c2 in connection_list:
        if c1 not in connections:
            connections[c1] = {c2}
        else:
            connections[c1].add(c2)
        if c2 not in connections:
            connections[c2] = {c1}
        else:
            connections[c2].add(c1)

    return connections


def solve(filename: str = os.path.join(MODULE_DIR, "input")) -> int:
    connection_list = load_input(filename)
    connections = group_connections(connection_list)

    groups = set()
    for c1, connection_set in connections.items():
        if not c1.startswith("t"):
            continue

        for c2, c3 in combinations(connection_set, 2):
            if c3 in connections[c2]:
                groups.add(tuple(sorted((c1, c2, c3))))

    return len(groups)


def main():
    assert solve(filename=os.path.join(MODULE_DIR, "test_input")) == 7
    print(solve())


if __name__ == "__main__":
    main()

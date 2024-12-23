import os

from puzzle_1 import group_connections, load_input
from tqdm import tqdm

MODULE_DIR = os.path.dirname(__file__)


def find_maximum_clique(connections: dict[str, set[str]], vertex: str) -> set[str]:
    max_len = max(len(edges) for edges in connections.values()) + 1
    clique = {vertex}
    for check_vertex, checked_edges in connections.items():
        if checked_edges & clique == clique:
            clique.add(check_vertex)

        if len(clique) == max_len:
            break

    return clique


def solve(filename: str = os.path.join(MODULE_DIR, "input")) -> str:
    connection_list = load_input(filename)
    connections = group_connections(connection_list)

    biggest_clique = []
    for vertex in tqdm(connections.keys()):
        if not (clique := find_maximum_clique(connections, vertex)):
            continue

        if len(clique) > len(biggest_clique):
            biggest_clique = clique

    return ",".join(sorted(biggest_clique))


def main():
    assert solve(filename=os.path.join(MODULE_DIR, "test_input")) == "co,de,ka,ta"
    print(solve())


if __name__ == "__main__":
    main()

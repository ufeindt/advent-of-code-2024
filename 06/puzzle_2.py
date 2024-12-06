from puzzle_1 import GuardMap
from tqdm import tqdm


def find_loops(filename: str = "06/input") -> int:
    map = GuardMap(filename=filename)
    map.run()

    loop_count = 0
    for x, y in tqdm(map.squares_visited):
        loop_map = GuardMap(filename=filename)
        if x == loop_map.guard["x"] and y == loop_map.guard["y"]:
            continue
        loop_map.map[y] = f"{loop_map.map[y][:x]}#{loop_map.map[y][x+1:]}"
        if not loop_map.run():
            loop_count += 1

    return loop_count


def main():
    assert find_loops("06/test_input") == 6
    print(find_loops())


if __name__ == "__main__":
    main()

def load_input(filename: str = "10/input") -> list[list[int]]:
    with open(filename) as f:
        return [[int(cell) for cell in line.strip()] for line in f.readlines()]


def find_trailheads(map: list[list[int]]) -> list[tuple[int, int]]:
    trailheads = []
    for y, line in enumerate(map):
        for x, cell in enumerate(line):
            if cell == 0:
                trailheads.append((x, y))

    return trailheads


def score_peaks(map: list[list[int]], x: int, y: int, elevation: int = 0) -> dict[tuple[int, int], int]:
    # print(x, y, elevation)
    if elevation == 9:
        return {(x, y): 1}

    peaks = {}
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        if (x1 := x+dx) < 0 or x1 > len(map[0])-1 or (y1 := y+dy) < 0 or y1 > len(map)-1:
            # print("out of bounds")
            continue

        if map[y1][x1] == elevation + 1:
            for peak, score in score_peaks(map, x1, y1, elevation=elevation+1).items():
                if peak not in peaks:
                    peaks[peak] = score
                else:
                    peaks[peak] += score
        # else:
        #     print("not the right way")

    return peaks


def solve(filename: str = "10/input") -> int:
    map = load_input(filename=filename)
    trailheads = find_trailheads(map)
    return sum(len(score_peaks(map, x, y)) for x, y in trailheads)


def main():
    assert solve(filename="10/test_input") == 36
    print(solve())


if __name__ == "__main__":
    main()

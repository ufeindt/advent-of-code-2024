from puzzle_1 import load_input, find_trailheads, score_peaks
import os


def solve(filename: str = "10/input") -> int:
    map = load_input(filename=filename)
    trailheads = find_trailheads(map)
    return sum(score for x, y in trailheads for score in score_peaks(map, x, y).values())


def main():
    assert solve(filename="10/test_input") == 81
    print(solve())


if __name__ == "__main__":
    main()

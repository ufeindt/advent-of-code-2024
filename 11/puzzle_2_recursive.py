from functools import cache

from puzzle_1 import load_input


@cache
def score(stone: int, n_blinks: int) -> int:
    if n_blinks == 0:
        return 1

    if stone == 0:
        new_stones = [1]
    elif (len_str := len(str(stone))) % 2 == 0:
        new_stones = [
            int(str(stone)[: len_str // 2]),
            int(str(stone)[len_str // 2 :]),
        ]
    else:
        new_stones = [stone * 2024]

    return sum(score(new_stone, n_blinks - 1) for new_stone in new_stones)


def solve(filename: str = "11/input", n_blinks: int = 75) -> int:
    stones = load_input(filename=filename)
    return sum(score(stone, n_blinks) for stone in stones)


def main():
    assert solve(filename="11/test_input", n_blinks=25) == 55312
    print(solve())


if __name__ == "__main__":
    main()

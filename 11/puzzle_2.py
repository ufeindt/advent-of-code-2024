from tqdm import tqdm


def load_input(filename: str = "11/input") -> dict[int, int]:
    with open(filename) as f:
        stones_in_line = [int(stone) for stone in f.readline().strip().split()]

    stones = {}
    for stone in stones_in_line:
        if stone not in stones:
            stones[stone] = 1
        else:
            stones[stone] += 1
    return stones


def blink(
    stones: dict[int, int], show_progress: bool = False, desc: str | None = None
) -> dict[int, int]:
    new_stones = {}

    if show_progress:
        iterator = tqdm(stones.items(), desc=desc)
    else:
        iterator = stones.items()

    for stone_value, stone_count in iterator:
        if stone_value == 0:
            new_stone_values = [1]
        elif (len_str := len(str(stone_value))) % 2 == 0:
            new_stone_values = [
                int(str(stone_value)[: len_str // 2]),
                int(str(stone_value)[len_str // 2 :]),
            ]
        else:
            new_stone_values = [stone_value * 2024]

        for new_value in new_stone_values:
            if new_value not in new_stones:
                new_stones[new_value] = stone_count
            else:
                new_stones[new_value] += stone_count

    return new_stones


def solve(
    filename: str = "11/input", show_progress: bool = True, n_blinks: int = 75
) -> int:
    stones = load_input(filename=filename)
    for k in range(n_blinks):
        stones = blink(stones, show_progress=show_progress, desc=f"Blink {k+1:>2}")

    return sum(stones.values())


def main():
    assert solve(filename="11/test_input", show_progress=False, n_blinks=25) == 55312
    print(solve())


if __name__ == "__main__":
    main()

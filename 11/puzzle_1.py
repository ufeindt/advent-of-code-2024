from tqdm import tqdm


def load_input(filename: str = "11/input") -> list[int]:
    with open(filename) as f:
        return [int(stone) for stone in f.readline().strip().split()]


def blink(
    stones: list[int], show_progress: bool = False, desc: str | None = None
) -> list[int]:
    new_stones = []

    if show_progress:
        iterator = tqdm(stones, desc=desc)
    else:
        iterator = stones

    for stone in iterator:
        if stone == 0:
            new_stones.append(1)
        elif (len_str := len(str(stone))) % 2 == 0:
            new_stones.extend(
                [int(str(stone)[: len_str // 2]), int(str(stone)[len_str // 2 :])]
            )
        else:
            new_stones.append(stone * 2024)

    return new_stones


def solve(
    filename: str = "11/input", show_progress: bool = True, n_blinks: int = 25
) -> int:
    stones = load_input(filename=filename)
    for k in range(n_blinks):
        stones = blink(stones, show_progress=show_progress, desc=f"Blink {k+1:>2}")

    return len(stones)


def main():
    assert solve(filename="11/test_input", show_progress=False) == 55312
    print(solve())


if __name__ == "__main__":
    main()

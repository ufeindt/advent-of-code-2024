from puzzle_1 import load_input


def generate_file_blocks(disk_map: str) -> list[tuple[int | None, int]]:
    file_blocks = []
    for k, block_length in enumerate(disk_map):
        if int(block_length) == 0:
            continue
        if k % 2 == 0:
            symbol = k // 2
        else:
            symbol = None
        file_blocks += [(symbol, int(block_length))]

    return file_blocks


def compact_files(file_blocks: list[str]) -> list[tuple[int | None, int]]:
    k = len(file_blocks) - 1
    while k >= 0:
        if file_blocks[k][0] is None:
            k -= 1
            continue

        for k_, block in enumerate(file_blocks[:k]):
            if block[0] is None and block[1] >= file_blocks[k][1]:
                if block[1] > file_blocks[k][1]:
                    extra_block = (None, block[1] - file_blocks[k][1])
                else:
                    extra_block = None
                file_blocks[k_] = file_blocks[k]
                file_blocks[k] = (None, file_blocks[k][1])
                if extra_block:
                    file_blocks = (
                        file_blocks[: k_ + 1] + [extra_block] + file_blocks[k_ + 1 :]
                    )
                    k += 1
                break
        k -= 1

    return file_blocks


def checksum(file_blocks: str) -> int:
    checksum = 0
    k = 0
    for block in file_blocks:
        if block[0]:
            checksum += sum(block[0] * (k_ + k) for k_ in range(block[1]))
        k += block[1]

    return checksum


def solve(filename: str = "09/input") -> int:
    return checksum(compact_files(generate_file_blocks(load_input(filename=filename))))


def main():
    assert solve(filename="09/test_input") == 2858
    print(solve())


if __name__ == "__main__":
    main()

def load_input(filename: str = "09/input") -> str:
    with open(filename) as f:
        input = f.readline().strip()

    return input


def generate_file_blocks(disk_map: str) -> list[int | None]:
    file_blocks = []
    for k, block_length in enumerate(disk_map):
        if k % 2 == 0:
            symbol = [k // 2]
        else:
            symbol = [None]
        file_blocks += symbol * int(block_length)

    return file_blocks


def compact_files(file_blocks: list[str]) -> list[int | None]:
    for k in range(len(file_blocks) - 1, -1, -1):
        if file_blocks[k] == [None]:
            continue

        if (empty_index := file_blocks.index(None)) > k:
            break

        file_blocks[empty_index] = file_blocks[k]
        file_blocks[k] = None

    return file_blocks


def checksum(file_blocks: str) -> int:
    return sum([k * b for k, b in enumerate(file_blocks) if b])


def solve(filename: str = "09/input") -> int:
    return checksum(compact_files(generate_file_blocks(load_input(filename=filename))))


def main():
    assert solve(filename="09/test_input") == 1928
    print(solve())


if __name__ == "__main__":
    main()

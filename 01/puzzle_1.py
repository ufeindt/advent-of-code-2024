def load_input_to_lists() -> tuple[list[int], list[int]]:
    with open("01/input.txt") as f:
        lines = [line.split() for line in f]

    return tuple([int(line[k]) for line in lines] for k in range(2))


if __name__ == "__main__":
    location_lists = load_input_to_lists()

    differences = [
        l2 - l1 for l1, l2 in zip(sorted(location_lists[0]), sorted(location_lists[1]))
    ]
    distances = [
        difference * (-1 if difference < 0 else 1) for difference in differences
    ]
    total_distance = sum(distances)
    print(total_distance)

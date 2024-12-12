from puzzle_1 import GardenMap


class GardenMapBulk(GardenMap):
    @staticmethod
    def get_region_perimeter(region: set[tuple[int, int]]) -> int:
        fence_sections = []
        for coords in region:
            for k, (dx, dy) in enumerate(((-1, 0), (0, -1), (1, 0), (0, 1))):
                if (coords[0] + dx, coords[1] + dy) not in region:
                    fence_sections.append((coords[0], coords[1], k))

        fence_sections = sorted(
            fence_sections, key=lambda s: (s[2], s[s[2] % 2], s[(s[2] + 1) % 2])
        )

        perimeter = 1
        for section_0, section_1 in zip(
            fence_sections[:-1], fence_sections[1:], strict=True
        ):
            index_eq = section_0[2] % 2
            index_inc = (section_0[2] + 1) % 2
            if (
                section_0[2] != section_1[2]
                or section_0[index_eq] != section_1[index_eq]
                or section_0[index_inc] + 1 != section_1[index_inc]
            ):
                perimeter += 1

        return perimeter


def solve(filename: str = "12/input") -> int:
    map = GardenMapBulk(filename=filename)
    return map.get_total_price()


def main():
    assert solve(filename="12/test_input") == 1206
    print(solve())


if __name__ == "__main__":
    main()

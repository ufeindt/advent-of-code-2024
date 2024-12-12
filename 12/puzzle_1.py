class GardenMap:
    def __init__(self, filename: str = "12/input"):
        with open(filename) as f:
            rows = [line.strip() for line in f]

        self.map = {
            (x, y): plant for y, row in enumerate(rows) for x, plant in enumerate(row)
        }
        self.coords_in_a_region = set()
        self.regions: list[set[tuple[int, int]]] = []

        self.find_all_regions()

    def find_region(
        self, coords: tuple[int, int], region: set[tuple[int, int]] | None = None
    ) -> set[tuple[int, int]]:
        if region is None:
            region = {coords}

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_coords = (coords[0] + dx, coords[1] + dy)

            if (
                next_coords not in self.map
                or self.map[next_coords] != self.map[coords]
                or next_coords in region
            ):
                continue
            else:
                region.add(next_coords)
                region |= self.find_region(next_coords, region=region)

        return region

    def find_all_regions(self):
        for coords in self.map.keys():
            if coords in self.coords_in_a_region:
                continue

            region = self.find_region(coords)
            self.regions.append(region)
            self.coords_in_a_region |= region

    @staticmethod
    def get_region_perimeter(region: set[tuple[int, int]]) -> int:
        perimeter = 0
        for coords in region:
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (coords[0] + dx, coords[1] + dy) not in region:
                    perimeter += 1

        return perimeter

    def get_total_price(self):
        return sum(
            len(region) * self.get_region_perimeter(region) for region in self.regions
        )


def solve(filename: str = "12/input") -> int:
    map = GardenMap(filename=filename)
    return map.get_total_price()


def main():
    assert solve(filename="12/test_input") == 1930
    print(solve())


if __name__ == "__main__":
    main()

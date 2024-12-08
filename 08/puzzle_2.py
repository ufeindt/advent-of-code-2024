from itertools import combinations
from puzzle_1 import AntennaMap


class AntennaMap2(AntennaMap):
    def find_antinodes(self):
        antinodes = set()
        for antenna_coordinates in self.antennas.values():
            for (x0, y0), (x1, y1) in combinations(antenna_coordinates, 2):
                dx = x1 - x0
                dy = y1 - y0

                for k_start, k_dir in ((0, 1), (-1, -1)):
                    k = k_start
                    while True:
                        if (
                                0 <= (xa := x0+k*dx) < self.width
                                and 0 <= (ya := y0+k*dy) < self.height
                        ):
                            antinodes.add((xa, ya))
                        else:
                            break
                        k += k_dir

        self._antinodes = antinodes


def main():
    test_map = AntennaMap2(filename="08/test_input")
    assert len(test_map.antinodes) == 34

    map = AntennaMap2()
    print(len(map.antinodes))


if __name__ == "__main__":
    main()

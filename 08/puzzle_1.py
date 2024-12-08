from itertools import combinations


class AntennaMap:
    def __init__(self, filename: str = "08/input"):
        with open(filename) as f:
            self._lines = [line.strip() for line in f]

        self.width = len(self._lines[0])
        self.height = len(self._lines)
        self._antennas = None
        self._antinodes = None

    def find_antinodes(self):
        antinodes = set()
        for antenna_coordinates in self.antennas.values():
            for (x0, y0), (x1, y1) in combinations(antenna_coordinates, 2):
                dx = x1 - x0
                dy = y1 - y0
                for k in (-1, 2):
                    if 0 <= (xa := x0+k*dx) < self.width and 0 <= (ya := y0+k*dy) < self.height:
                        antinodes.add((xa, ya))

        self._antinodes = antinodes

    def map_antennas(self):
        antennas = {}
        for y, line in enumerate(self._lines):
            for x, frequency in enumerate(line):
                if frequency == ".":
                    continue
                if frequency not in antennas:
                    antennas[frequency] = [(x, y)]
                else:
                    antennas[frequency].append((x, y))

        self._antennas = antennas

    @property
    def antennas(self):
        if self._antennas is None:
            self.map_antennas()

        return self._antennas

    @property
    def antinodes(self):
        if self._antinodes is None:
            self.find_antinodes()

        return self._antinodes


def main():
    test_map = AntennaMap(filename="08/test_input")
    assert len(test_map.antinodes) == 14

    map = AntennaMap()
    print(len(map.antinodes))


if __name__ == "__main__":
    main()

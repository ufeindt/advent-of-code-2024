from copy import copy
from enum import Enum


class StepResult(Enum):
    MOVED = 1
    TURNED = 2
    LEFT_MAP = 3


class GuardMap:
    directions = {
        "^": {"move": (0, -1), "turn": ">"},
        ">": {"move": (1, 0), "turn": "v"},
        "v": {"move": (0, 1), "turn": "<"},
        "<": {"move": (-1, 0), "turn": "^"},
    }

    def __init__(self, filename: str = "06/input"):
        with open(filename) as f:
            self.map = [line.strip() for line in f]

        for y, row in enumerate(self.map):
            if guard_symbol := [a for a in row if a in self.directions]:
                self.guard = {
                    "facing": guard_symbol[0],
                    "x": row.index(guard_symbol[0]),
                    "y": y,
                }
                self.map[y] = row.replace(guard_symbol[0], "X")
                break

    def run(self) -> bool:
        guard_history = {copy(self.guard_tuple)}
        step_result = None
        while step_result != StepResult.LEFT_MAP:
            step_result = self.step()
            if self.guard_tuple in guard_history and step_result != StepResult.LEFT_MAP:
                return False
            guard_history.add(copy(self.guard_tuple))
        return True

    def step(self) -> StepResult:
        move = self.directions[self.guard["facing"]]["move"]
        turn = self.directions[self.guard["facing"]]["turn"]
        next_x = self.guard["x"] + move[0]
        next_y = self.guard["y"] + move[1]

        if next_x < 0 or next_x > self.max_x or next_y < 0 or next_y > self.max_y:
            return StepResult.LEFT_MAP
        elif self.map[next_y][next_x] == "#":
            self.guard["facing"] = turn
            return StepResult.TURNED
        else:
            self.guard["x"], self.guard["y"] = next_x, next_y
            self.map[next_y] = (
                f"{self.map[next_y][:next_x]}X{self.map[next_y][next_x+1:]}"
            )
            return StepResult.MOVED

    @property
    def guard_tuple(self) -> tuple[int, int, str]:
        return (self.guard["x"], self.guard["y"], self.guard["facing"])

    @property
    def max_x(self) -> int:
        return len(self.map[0]) - 1

    @property
    def max_y(self) -> int:
        return len(self.map) - 1

    @property
    def squares_visited(self) -> list[tuple[int, int]]:
        squares = []
        for y, row in enumerate(self.map):
            for x, symbol in enumerate(row):
                if symbol == "X":
                    squares.append((x, y))
        return squares


def main():
    test_map = GuardMap(filename="06/test_input")
    test_map.run()
    assert len(test_map.squares_visited) == 41

    map = GuardMap()
    map.run()
    print(len(map.squares_visited))


if __name__ == "__main__":
    main()

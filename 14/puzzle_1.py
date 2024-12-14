from pydantic import BaseModel
import re


class Robot(BaseModel):
    x: int
    y: int
    v_x: int
    v_y: int


def load_input(filename: str = "14/input") -> list[Robot]:
    pattern = r"p\=(\d+)\,(\d+) v\=(-?\d+)\,(-?\d+)"
    with open(filename) as f:
        robots = [
            Robot(x=match[0], y=match[1], v_x=match[2], v_y=match[3])
            for match in re.findall(pattern, f.read())
        ]

    return robots


def move_robots(
    robots: list[Robot], dt: int = 100, width: int = 101, height: int = 103
) -> list[Robot]:
    for robot in robots:
        robot.x = (robot.x + dt * robot.v_x) % width
        robot.y = (robot.y + dt * robot.v_y) % height

    return robots


def safety_score(robots: list[Robot], width: int = 101, height: int = 103) -> int:
    return (
        len([r for r in robots if r.x < width // 2 and r.y < height // 2])
        * len([r for r in robots if r.x > width // 2 and r.y < height // 2])
        * len([r for r in robots if r.x < width // 2 and r.y > height // 2])
        * len([r for r in robots if r.x > width // 2 and r.y > height // 2])
    )


def print_map(
    robots: list[Robot], width: int = 101, height: int = 103, block_middle: bool = False
):
    for y in range(height):
        if block_middle and y == height // 2:
            print()
            continue

        cell_count: list[int | str] = [
            len([r for r in robots if r.x == x and r.y == y]) for x in range(width)
        ]
        if block_middle:
            cell_count[width // 2] = " "

        print("".join([str(c) if c else "." for c in cell_count]))


def solve(filename: str = "14/input", width: int = 101, height: int = 103) -> int:
    robots = load_input(filename=filename)
    robots = move_robots(robots, width=width, height=height)
    return safety_score(robots, width=width, height=height)


def main():
    assert solve(filename="14/test_input", width=11, height=7) == 12
    print(solve())


if __name__ == "__main__":
    main()

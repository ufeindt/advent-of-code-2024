import re
from pydantic import BaseModel


class ClawMachine(BaseModel):
    a_x: int
    a_y: int
    b_x: int
    b_y: int
    price_x: int
    price_y: int


def load_input(filename: str = "13/input") -> list[ClawMachine]:
    pattern = r"X[\=\+]([0-9]+), Y[\=\+]([0-9]+)"
    machines = []
    a_x, a_y, b_x, b_y = None, None, None, None
    with open(filename) as f:
        for line in f.readlines():
            if line.startswith("Button A"):
                a_x, a_y = re.findall(pattern, line)[0]
            elif line.startswith("Button B"):
                b_x, b_y = re.findall(pattern, line)[0]
            elif line.startswith("Prize"):
                price_x, price_y = re.findall(pattern, line)[0]
                machines.append(
                    ClawMachine(
                        a_x=a_x,
                        a_y=a_y,
                        b_x=b_x,
                        b_y=b_y,
                        price_x=price_x,
                        price_y=price_y,
                    )
                )

    return machines


def find_machine_cost(machine: ClawMachine) -> int:
    det = machine.a_x * machine.b_y - machine.a_y * machine.b_x
    n_a = (machine.b_y * machine.price_x - machine.b_x * machine.price_y) / det
    n_b = (machine.a_x * machine.price_y - machine.a_y * machine.price_x) / det

    if n_a.is_integer() and n_b.is_integer():
        return 3 * int(n_a) + int(n_b)

    return 0


def solve(filename: str = "13/input", offset: int | None = None) -> int:
    machines = load_input(filename=filename)
    if offset:
        for machine in machines:
            machine.price_x += offset
            machine.price_y += offset
    return sum(find_machine_cost(machine) for machine in machines)


def main():
    assert solve(filename="13/test_input") == 480
    print(solve())


if __name__ == "__main__":
    main()

from pydantic import BaseModel


class Computer(BaseModel):
    register_a: int
    register_b: int
    register_c: int
    program: list[int]
    pointer: int = 0
    output: list[int] = []

    def get_combo_value(self, operand: int) -> int:
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.register_a
            case 5:
                return self.register_b
            case 6:
                return self.register_c
            case 7:
                raise ValueError("Reserved combo operand 7")

        raise ValueError(f"Unknown combo operand {operand}")

    def run_instructions(self):
        while self.pointer < len(self.program) - 1:
            opcode, operand = self.program[self.pointer : self.pointer + 2]
            match opcode:
                case 0:
                    self.adv(operand)
                case 1:
                    self.bxl(operand)
                case 2:
                    self.bst(operand)
                case 3:
                    self.jnz(operand)
                case 4:
                    self.bxc()
                case 5:
                    self.out(operand)
                case 6:
                    self.bdv(operand)
                case 7:
                    self.cdv(operand)

            self.pointer += 2
            continue
            print(
                opcode,
                operand,
                self.register_a,
                self.register_a % 8,
                self.register_b,
                self.register_b % 8,
                self.register_c,
                self.register_c % 8,
                self.output,
            )

    def adv(self, operand: int):
        value = self.get_combo_value(operand)
        self.register_a //= 2**value

    def bxl(self, operand: int):
        self.register_b ^= operand

    def bst(self, operand: int):
        value = self.get_combo_value(operand)
        self.register_b = value % 8

    def jnz(self, operand: int):
        if self.register_a != 0:
            self.pointer = operand - 2

    def bxc(self):
        self.register_b ^= self.register_c

    def out(self, operand: int):
        self.output.append(self.get_combo_value(operand) % 8)

    def bdv(self, operand: int):
        value = self.get_combo_value(operand)
        self.register_b = self.register_a // 2**value

    def cdv(self, operand: int):
        value = self.get_combo_value(operand)
        self.register_c = self.register_a // 2**value


def load_input(filename="17/input") -> Computer:
    input = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("Register"):
                register_id = line.split(":")[0][-1].lower()
                input[f"register_{register_id}"] = line.split(":")[1].strip()
            elif line.startswith("Program"):
                input["program"] = line.split(":")[1].strip().split(",")

    return Computer(**input)


def solve(filename="17/input") -> str:
    computer = load_input(filename=filename)
    computer.run_instructions()
    return ",".join([str(o) for o in computer.output])


def main():
    assert solve(filename="17/test_input") == "4,6,3,5,6,3,5,2,1,0"
    print(solve())


if __name__ == "__main__":
    main()

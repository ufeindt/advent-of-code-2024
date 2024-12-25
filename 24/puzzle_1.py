from copy import deepcopy
import os
import re
from typing import Literal
import random

from pydantic import BaseModel

MODULE_DIR = os.path.dirname(__file__)


class Gate(BaseModel):
    name: str
    output: bool | None = None
    input: tuple[str, str] | None = None
    gate_type: Literal["AND", "OR", "XOR"] | None = None

    def __str__(self):
        out = f"Gate: {self.name}"
        if self.input and self.gate_type:
            out += f" = {self.input[0]} {self.gate_type} {self.input[1]}"
        if self.output:
            out += f" Output: {self.output}"

        return f"<{out}>"

    def determine_output(self, v1: bool, v2: bool):
        match self.gate_type:
            case "AND":
                self.output = v1 and v2
            case "OR":
                self.output = v1 or v2
            case "XOR":
                self.output = v1 ^ v2


class Circuit(BaseModel):
    gates: dict[str, Gate]

    def get_gate_output(self, name: str) -> bool:
        gate = self.gates[name]

        if gate.output is None:
            if gate.input is None:
                raise ValueError("Gate has no inputs")
            gate.determine_output(
                *(self.get_gate_output(input_name) for input_name in gate.input)
            )

        if gate.output is None:
            raise ValueError("Output was not set")

        return gate.output

    def get_register_number(self, register: str) -> int:
        value = 0
        for gate_name in self.gates.keys():
            if gate_name.startswith(register) and self.get_gate_output(gate_name):
                value += 1 << int(gate_name[1:])

        return value

    def get_all_gate_parents(self, name: str) -> set[str]:
        gate = self.gates[name]
        if not gate.input:
            return set()

        parents = {*gate.input}
        for input_name in gate.input:
            parents |= self.get_all_gate_parents(input_name)

        return parents

    def reset_outputs(self):
        for gate in self.gates.values():
            if gate.input:
                gate.output = None

    def set_random_inputs(self):
        for gate in self.gates.values():
            if gate.name[0] in "xy":
                gate.output = bool(random.getrandbits(1))

    def swap_gate_outputs(self, name_1: str, name_2: str):
        if name_1 in self.get_all_gate_parents(
            name_2
        ) or name_2 in self.get_all_gate_parents(name_1):
            raise ValueError("Swap would create loop")

        gate_1 = deepcopy(self.gates[name_1])
        gate_2 = deepcopy(self.gates[name_2])

        gate_1.name = name_2
        gate_2.name = name_1

        self.gates[name_1] = gate_2
        self.gates[name_2] = gate_1

    @property
    def target_number(self) -> int:
        return self.get_register_number("x") + self.get_register_number("y")

    @property
    def output_number(self) -> int:
        return self.get_register_number("z")

    # @propert
    # def incorrect_output_gates(self) -> list[str]:
    #     correct_bits = self.target_number ^ self.output_number
    #     incorrect = []
    #     for gate in self.gates.values():
    #         if (
    #             gate.name.startswith("z")
    #             and (correct_bits >> int(gate.name[1:])) % 2 == 1
    #         ):
    #             incorrect.append(gate.name)
    #
    #     return sorted(incorrect)

    @property
    def suspicious_gates(self) -> set[str]:
        max_z = max(
            int(gate.name[1:])
            for gate in self.gates.values()
            if gate.name.startswith("z")
        )

        suspicious = set()
        # All but last output wire must be from XOR Gate
        for k in range(max_z - 1):
            gate = self.gates[f"z{k:02}"]
            if gate.gate_type != "XOR":
                # print(gate)
                suspicious.add(gate.name)

        # Last output wire is from an OR gate
        gate = self.gates[f"z{max_z:02}"]
        if gate.gate_type != "OR":
            suspicious.add(gate.name)

        # XOR gates take x and y wires or output z wire
        for gate in self.gates.values():
            if not gate.input or gate.gate_type != "XOR":
                continue
            if (gate.input[0][0], gate.input[1][0]) in (("x", "y"), ("y", "x")):
                continue
            if not gate.name.startswith("z"):
                # print(gate)
                suspicious.add(gate.name)

        # XOR only takes an input bit if a XOR follows it, unless the input bits are the first bits
        for gate in self.gates.values():
            if not gate.input or gate.gate_type != "XOR":
                continue
            if (gate.input[0][0], gate.input[1][0]) not in (
                ("x", "y"),
                ("y", "x"),
            ) or gate.input in (("x00", "y00"), ("y00", "x00")):
                continue

            connecting_gates = [
                g for g in self.gates.values() if g.input and gate.name in g.input
            ]
            if len([g for g in connecting_gates if g.gate_type == "XOR"]) != 1:
                suspicious.add(gate.name)

        # AND gate only connect to OR gates unless inputs are x and y wires
        for gate in self.gates.values():
            if not gate.input or gate.gate_type != "AND":
                continue
            if gate.input in (("x00", "y00"), ("y00", "x00")):
                continue
            connecting_gates = [
                g for g in self.gates.values() if g.input and gate.name in g.input
            ]
            if [g for g in connecting_gates if g.gate_type != "OR"]:
                suspicious.add(gate.name)

        return suspicious


def load_input(filename: str = os.path.join(MODULE_DIR, "input")) -> dict[str, Gate]:
    with open(filename) as f:
        start_wires, connected_gates = f.read().split("\n\n")

    gates = [
        Gate(name=name, output=int(value))
        for name, value in re.findall(r"([a-z0-9]{3}): ([01])", start_wires)
    ] + [
        Gate(name=name, input=(v1, v2), gate_type=gate_type)
        for v1, gate_type, v2, name in re.findall(
            r"([a-z0-9]{3}) (AND|OR|XOR) ([a-z0-9]{3}) -> ([a-z0-9]{3})",
            connected_gates,
        )
    ]

    return {gate.name: gate for gate in gates}


def solve(filename: str = os.path.join(MODULE_DIR, "input")) -> int:
    gates = load_input(filename)
    circuit = Circuit(gates=gates)

    return circuit.output_number


def main():
    assert solve(filename=os.path.join(MODULE_DIR, "test_input")) == 2024
    print(solve())


if __name__ == "__main__":
    main()

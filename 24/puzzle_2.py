import os
from copy import deepcopy
from itertools import combinations

from puzzle_1 import Circuit, load_input

MODULE_DIR = os.path.dirname(__file__)


def solve(filename: str = os.path.join(MODULE_DIR, "input")) -> str:
    gates = load_input(filename)
    circuit = Circuit(gates=deepcopy(gates))

    gate_combos = list(combinations(circuit.suspicious_gates, 2))
    swap_sets = list(combinations(gate_combos, 4))
    swap_sets = [
        swap_set
        for swap_set in swap_sets
        if len({combo for combos in swap_set for combo in combos}) == 8
    ]

    solutions = []
    for swap_set in swap_sets:
        circuit = Circuit(gates=load_input(filename))
        try:
            for swap in swap_set:
                circuit.swap_gate_outputs(*swap)
        except ValueError:
            continue

        test_passed = True
        for _ in range(100):
            circuit.reset_outputs()
            circuit.set_random_inputs()
            if circuit.output_number != circuit.target_number:
                test_passed = False
                break

        if test_passed:
            solutions.append(swap_set)

    answers = {
        ",".join(sorted([combo for swap in swap_set for combo in swap]))
        for swap_set in solutions
    }
    return "\n".join(answers)


def main():
    print(solve())


if __name__ == "__main__":
    main()

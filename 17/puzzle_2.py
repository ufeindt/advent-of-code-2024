from puzzle_1 import load_input


def solve(filename="17/input") -> int:
    computer = load_input(filename=filename)
    solutions = [0]
    targets = [computer.program[-k:] for k in range(1, len(computer.program) + 1)]
    for target in targets:
        new_solutions = []
        for solution in solutions:
            for a_ in range(8):
                a = 8 * solution + a_
                computer = load_input(filename=filename)
                computer.register_a = a
                computer.run_instructions()
                if computer.output == target:
                    new_solutions.append(a)
        solutions = new_solutions

    return min(solutions)


def main():
    assert solve(filename="17/part_2_test_input") == 117440
    print(solve())


if __name__ == "__main__":
    main()

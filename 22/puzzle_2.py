import os

from puzzle_1 import load_input, next_secret

MODULE_DIR = os.path.dirname(__file__)


def solve(filename: str = os.path.join(MODULE_DIR, "input")) -> int:
    secrets = load_input(filename)

    sequence_outcomes = []
    for secret in secrets:
        sequences = {}
        current_sequence = (None, None, None, None)
        for _ in range(2000):
            new_secret = next_secret(secret)
            current_sequence = (
                current_sequence[1],
                current_sequence[2],
                current_sequence[3],
                (new_secret % 10) - (secret % 10),
            )
            if None not in current_sequence and current_sequence not in sequences:
                sequences[current_sequence] = new_secret % 10

            secret = new_secret

        sequence_outcomes.append(sequences)

    all_sequences = {
        sequence for sequences in sequence_outcomes for sequence in sequences
    }
    return max(
        sum(sequences.get(sequence, 0) for sequences in sequence_outcomes)
        for sequence in all_sequences
    )


def main():
    assert solve(filename=os.path.join(MODULE_DIR, "part_2_test_input")) == 23
    print(solve())


if __name__ == "__main__":
    main()

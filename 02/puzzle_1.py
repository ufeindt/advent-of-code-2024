def load_input() -> list[list[int]]:
    with open("02/input.txt") as f:
        lines = [line.split() for line in f]

    return [[int(value.strip()) for value in line] for line in lines]


def is_report_safe(report: list[int], tolerance: int = 0) -> bool:
    if tolerance < 0:
        return False

    latest_value = report[0]
    for k, current_value in enumerate(report[1:]):
        if k == 0:
            direction = 1 if current_value > latest_value else -1

        if (change := (current_value - latest_value) * direction) > 3 or change <= 0:
            return (
                is_report_safe(report[:k+1] + report[k+2:], tolerance=tolerance - 1) or
                is_report_safe(report[:k] + report[k+1:], tolerance=tolerance - 1) or
                is_report_safe(report[1:], tolerance=tolerance - 1)
            )

        latest_value = current_value

    return True


if __name__ == "__main__":
    reports = load_input()

    print(sum(is_report_safe(report) for report in reports))

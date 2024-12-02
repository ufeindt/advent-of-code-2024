from puzzle_1 import is_report_safe, load_input

if __name__ == "__main__":
    reports = load_input()

    print(sum(is_report_safe(report, tolerance=1) for report in reports))

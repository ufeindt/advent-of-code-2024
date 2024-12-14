from collections import Counter

from puzzle_1 import Robot, load_input, move_robots, print_map


def variance(robots):
    x_mean = sum(r.x for r in robots) / len(robots)
    y_mean = sum(r.y for r in robots) / len(robots)
    x_var = sum((r.x - x_mean) ** 2 for r in robots) / len(robots)
    y_var = sum((r.y - y_mean) ** 2 for r in robots) / len(robots)

    return x_var, y_var


def main():
    robots = load_input()
    x_vars = []
    y_vars = []
    for _ in range(103):
        x_var, y_var = variance(robots)
        x_vars.append(x_var)
        y_vars.append(y_var)
        move_robots(robots, dt=1)

    index_x_min = x_vars.index(min(x_vars))
    index_y_min = y_vars.index(min(y_vars))

    timestamps = []
    for start, step in [(index_x_min, 101), (index_y_min, 103)]:
        timestamps.extend(list(range(start, start + step**2, step)))

    counts = Counter(timestamps)
    for t in {t for t, c in counts.items() if c > 1}:
        robots = move_robots(load_input(), dt=t)
        print(t, variance(robots))
        print_map(robots)
        print()


if __name__ == "__main__":
    main()

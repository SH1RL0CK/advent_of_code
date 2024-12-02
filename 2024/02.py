from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=2)
input_data = puzzle.input_data.splitlines()
example_input_data = puzzle.examples[0].input_data.splitlines()


def is_safe(report):
    is_increasing = all(
        0 < report[i + 1] - report[i] <= 3 for i in range(len(report) - 1)
    )
    is_decreasing = all(
        0 < report[i] - report[i + 1] <= 3 for i in range(len(report) - 1)
    )
    return is_increasing or is_decreasing


def can_be_made_safe(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            return True
    return False


def part_a(data):
    safe = 0
    for line in data:
        line = [int(x) for x in line.split(" ")]
        if is_safe(line):
            safe += 1
    return safe


def part_b(data):
    safe = 0
    for line in data:
        line = [int(x) for x in line.split(" ")]
        if is_safe(line) or can_be_made_safe(line):
            safe += 1
    return safe


if __name__ == "__main__":
    answer_a = part_a(input_data)
    print(f"Answer A: {answer_a}")
    puzzle.answer_a = answer_a
    answer_b = part_b(input_data)
    print(f"Answer B: {answer_b}")
    puzzle.answer_b = answer_b

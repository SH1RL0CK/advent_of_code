from aocd.models import Puzzle

puzzle = Puzzle(2022, 6)
input_data = puzzle.input_data


def part_a():
    for i in range(4, len(input_data)):
        if len(set(input_data[i - 4 : i])) == 4:
            return i


def part_b():
    for i in range(14, len(input_data)):
        if len(set(input_data[i - 14 : i])) == 14:
            return i


if __name__ == "__main__()":
    puzzle.answer_a = part_a()
    puzzle.answer_b = part_b()

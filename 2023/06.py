import math
import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=6)
input_data = puzzle.input_data.splitlines()
example_input_data = puzzle.examples[0].input_data.splitlines()


def parse_line_a(line):
    return [int(i) for i in re.sub(" +", " ", line.split(": ")[1]).split(" ")[1:]]


def get_number_of_solutions(time, distance):
    determinant = time**2 - 4 * distance
    solution_1 = (time - math.sqrt(determinant)) / 2
    solution_2 = (time + math.sqrt(determinant)) / 2
    if solution_1 == math.ceil(solution_1):
        solution_1 += 1
    if solution_2 == math.floor(solution_2):
        solution_2 -= 1
    solution_1 = math.ceil(solution_1)
    solution_2 = math.floor(solution_2)
    return solution_2 - solution_1 + 1


def part_a(data):
    times = parse_line_a(data[0])
    distances = parse_line_a(data[1])
    result = 1
    for time, distance in zip(times, distances):
        result *= get_number_of_solutions(time, distance)
    return result


def parse_line_b(line):
    return int(line.split(": ")[1].replace(" ", ""))


def part_b(data):
    time = parse_line_b(data[0])
    distance = parse_line_b(data[1])
    return get_number_of_solutions(time, distance)


if __name__ == "__main__":
    answer_a = part_a(input_data)
    print(f"Answer A: {answer_a}")
    answer_b = part_b(input_data)
    print(f"Answer B: {answer_b}")
    puzzle.answer_a = answer_a
    puzzle.answer_b = answer_b

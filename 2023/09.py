import operator
from functools import reduce

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=9)
input_data = puzzle.input_data.splitlines()
example_input_data = puzzle.examples[0].input_data.splitlines()


def part_a(data):
    result = 0
    for line in data:
        numbers = [[int(n) for n in line.split(" ")]]
        while not all([number == 0 for number in numbers[-1]]):
            numbers.append([numbers[-1][i] - numbers[-1][i-1] for i in range(1, len(numbers[-1]))])
        result += sum([n[-1] for n in numbers])
    return result


def part_b(data):
    result = 0
    for line in data:
        numbers = [[int(n) for n in line.split(" ")]]
        while not all([number == 0 for number in numbers[-1]]):
            numbers.append([numbers[-1][i] - numbers[-1][i-1] for i in range(1, len(numbers[-1]))])
        number = numbers[-2][0]
        for n in list(reversed(numbers))[2:]:
            number = n[0] - number
        result += number
    return result


if __name__ == '__main__':
    answer_a = part_a(input_data)
    print(f"Answer A: {answer_a}")
    puzzle.answer_a = answer_a
    answer_b = part_b(input_data)
    print(f"Answer B: {answer_b}")
    puzzle.answer_b = answer_b
import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=1)
input_data = puzzle.input_data.splitlines()
example_input_data = puzzle.examples[0].input_data.splitlines()


def part_a():
    result = 0
    for line in input_data:
        numbers = re.findall(r"\d", line)
        number = int(f"{numbers[0]}{numbers[-1]}")
        result += number
    return result


def part_b():
    result = 0
    for line in input_data:
        numbers = re.findall(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
        )
        number = convert_number(numbers[0]) * 10 + convert_number(numbers[-1])
        result += number
    return result


def convert_number(number):
    numbers_as_words = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    return numbers_as_words.index(number) + 1 if len(number) > 1 else int(number)


if __name__ == "__main__":
    answer_a = part_a()
    print(f"Answer A: {answer_a}")
    answer_b = part_b()
    print(f"Answer B: {answer_b}")
    puzzle.answer_a = answer_a
    puzzle.answer_b = answer_b

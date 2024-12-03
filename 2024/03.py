import os
import re
import sys

from aocd.models import Puzzle

from utils import *

puzzle = Puzzle(year=2024, day=3)
input_data = puzzle.input_data.splitlines()
example_input_data = puzzle.examples[0].input_data.splitlines()


def part_a(data):
    result = 0
    for line in data:
        instructions = re.findall(r"mul\(?[0-9]{1,3}\,?[0-9]{1,3}\)", line)
        numbers = list(parsing.ints(i) for i in instructions)
        result += sum(math_utils.product(n) for n in numbers)
    return result


def part_b(data):
    result = 0
    disable = False
    for line in data:
        instructions = re.findall(
            r"mul\(?[0-9]{1,3}\,?[0-9]{1,3}\)|do\(\)|don't\(\)", line
        )
        for i in instructions:
            if "don't" in i:
                disable = True
            elif "do" in i:
                disable = False
            elif not disable:
                result += math_utils.product(parsing.ints(i))
    return result


if __name__ == "__main__":
    match os.environ.get("MODE"):
        case "part_a_example":
            answer_a = part_a(example_input_data)
            print(f"Answer A: {answer_a}")
        case "part_a":
            answer_a = part_a(input_data)
            print(f"Answer A: {answer_a}")
            puzzle.answer_a = answer_a
        case "part_b_example":
            example_input_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))".splitlines()
            answer_b = part_b(example_input_data)
            print(f"Answer B: {answer_b}")
        case "part_b":
            answer_b = part_b(input_data)
            print(f"Answer B: {answer_b}")
            puzzle.answer_b = answer_b
        case _:
            print("No MODE set")

import os

import numpy as np
from aocd.models import Puzzle

from utils import *

puzzle = Puzzle(year=2024, day=4)
input_data = puzzle.input_data.splitlines()
example_input_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".splitlines()


def get_lines(matrix):
    horizontal_lines = [list(row) for row in matrix]

    vertical_lines = [list(col) for col in zip(*matrix)]

    diagonals_lr = [
        list(np.diagonal(matrix, offset=i))
        for i in range(-len(matrix) + 1, len(matrix[0]))
    ]

    flipped_matrix = np.fliplr(matrix)
    diagonals_rl = [
        list(np.diagonal(flipped_matrix, offset=i))
        for i in range(-len(matrix) + 1, len(matrix[0]))
    ]

    return horizontal_lines + vertical_lines + diagonals_lr + diagonals_rl


def part_a(data):
    result = 0
    matrix = np.array([list(row) for row in data])
    lines = ["".join(line) for line in get_lines(matrix)]
    for line in lines:
        result += line.count("XMAS")
        result += line[::-1].count("XMAS")
    return result


def part_b(data):
    data = NoNegatives([NoNegatives(row) for row in data])
    result = 0
    rows, cols = len(data), len(data[0])
    for y in range(rows):
        for x in range(cols):
            if data[y][x] != "A":
                continue
            try:
                word = (
                    data[y - 1][x - 1]
                    + data[y - 1][x + 1]
                    + data[y + 1][x - 1]
                    + data[y + 1][x + 1]
                )
                if word in ["MMSS", "SMSM", "SSMM", "MSMS"]:
                    result += 1
            except:
                continue
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
            answer_b = part_b(example_input_data)
            print(f"Answer B: {answer_b}")
        case "part_b":
            answer_b = part_b(input_data)
            print(f"Answer B: {answer_b}")
            puzzle.answer_b = answer_b
        case _:
            print("No MODE set")

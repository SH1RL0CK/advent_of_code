import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=3)
input_data = puzzle.input_data.splitlines()
example_input_data = puzzle.examples[0].input_data.splitlines()


def part_a():
    sum = 0
    for i, line in enumerate(input_data):
        for number in re.finditer(r"\d+", line):
            if is_part_number(input_data, i, number.start(), number.end() - 1):
                sum += int(number.group())
    return sum


def is_part_number(input_data, y, x_start, x_end):
    surrounding_symbols = ""
    s_x_start = x_start - 1
    s_x_end = x_end + 1

    if x_start > 0:
        surrounding_symbols += input_data[y][s_x_start]
    else:
        s_x_start = x_start

    if x_end < len(input_data[y]) - 1:
        surrounding_symbols += input_data[y][s_x_end]
    else:
        s_x_end = x_end

    if y > 0:
        surrounding_symbols += input_data[y - 1][s_x_start : s_x_end + 1]
    if y < len(input_data) - 1:
        surrounding_symbols += input_data[y + 1][s_x_start : s_x_end + 1]

    return any(symbol != "." for symbol in surrounding_symbols)


def part_b():
    gears = dict()
    sum = 0
    for i, line in enumerate(input_data):
        for number in re.finditer(r"\d+", line):
            surrounding_gears = get_surrounding_gears(
                input_data, i, number.start(), number.end() - 1
            )
            for gear in surrounding_gears:
                if gear not in gears:
                    gears[gear] = [int(number.group())]
                else:
                    gears[gear].append(int(number.group()))
    for gear in gears.values():
        if len(gear) == 2:
            sum += gear[0] * gear[1]

    return sum


def get_surrounding_gears(input_data, y, x_start, x_end):
    surrounding_symbols = []
    s_x_start = x_start - 1
    s_x_end = x_end + 1

    if x_start > 0:
        surrounding_symbols.append((y, s_x_start))
    else:
        s_x_start = x_start

    if x_end < len(input_data[y]) - 1:
        surrounding_symbols.append((y, s_x_end))
    else:
        s_x_end = x_end

    if y > 0:
        surrounding_symbols += [(y - 1, i) for i in range(s_x_start, s_x_end + 1)]
    if y < len(input_data) - 1:
        surrounding_symbols += [(y + 1, i) for i in range(s_x_start, s_x_end + 1)]

    return [cor for cor in surrounding_symbols if input_data[cor[0]][cor[1]] == "*"]


if __name__ == "__main__":
    answer_a = part_a()
    print(f"Answer A: {answer_a}")
    answer_b = part_b()
    print(f"Answer B: {answer_b}")
    puzzle.answer_a = answer_a
    puzzle.answer_b = answer_b

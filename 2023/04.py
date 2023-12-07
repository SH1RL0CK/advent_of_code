import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=4)
input_data = puzzle.input_data.splitlines()
example_input_data = puzzle.examples[0].input_data.splitlines()


def part_a():
    result = 0
    for line in input_data:
        line = re.sub(" +", " ", line).split(": ")[1].split(" | ")
        winning_numbers = line[0].split(" ")
        my_numbers = line[1].split(" ")
        matching = len(set(winning_numbers).intersection(my_numbers))
        if matching > 0:
            result += pow(2, matching - 1)
    return result


total_count_b = 0


def part_b():
    for i in range(len(input_data)):
        play_card(i)
    return total_count_b


def play_card(i):
    global total_count_b
    total_count_b += 1
    line = input_data[i]
    line = re.sub(" +", " ", line).split(": ")[1].split(" | ")
    winning_numbers = line[0].split(" ")
    my_numbers = line[1].split(" ")
    matching = len(set(winning_numbers).intersection(my_numbers))
    for j in range(i + 1, i + matching + 1):
        play_card(j)


if __name__ == "__main__":
    answer_a = part_a()
    print(f"Answer A: {answer_a}")
    answer_b = part_b()
    print(f"Answer B: {answer_b}")
    puzzle.answer_a = answer_a
    puzzle.answer_b = answer_b

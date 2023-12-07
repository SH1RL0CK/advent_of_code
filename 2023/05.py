from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=5)
input_data = puzzle.input_data.split("\n\n")
example_input_data = puzzle.examples[0].input_data.split("\n\n")


def get_lowest_location(data, values):
    for block in data[1:]:
        modified = []
        for line in block.splitlines()[1:]:
            destination, source, range_len = [int(i) for i in line.split(" ")]
            for i, value in enumerate(values):
                if (source <= value < (source + range_len)) and i not in modified:
                    values[i] += destination - source
                    modified.append(i)
                    print(values)
    return min(values)


def part_a():
    data = input_data
    values = [int(i) for i in data[0].split(": ")[1].split(" ")]
    return get_lowest_location(data, values)


if __name__ == "__main__":
    answer_a = part_a()
    print(f"Answer A: {answer_a}")
    puzzle.answer_a = answer_a

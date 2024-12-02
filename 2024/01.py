from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=1)
input_data = puzzle.input_data.splitlines()
example_input_data = puzzle.examples[0].input_data.splitlines()


def part_a(data):
    left = []
    right = []
    for line in data:
        line = line.split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))
    left.sort()
    right.sort()
    print(left)
    print(right)
    return sum(abs(y - x) for x, y in zip(left, right))


def part_b(data):
    left = []
    right = []
    for line in data:
        line = line.split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))
    return sum(x * right.count(x) for x in left)


if __name__ == "__main__":
    answer_a = part_a(input_data)
    print(f"Answer A: {answer_a}")
    puzzle.answer_a = answer_a
    answer_b = part_b(input_data)
    print(f"Answer B: {answer_b}")
    puzzle.answer_b = answer_b

from aocd.models import Puzzle

puzzle = Puzzle(2022, 7)
input_data = puzzle.input_data.splitlines()


def parse():
    dirs = []
    current_dirs = []
    for line in input_data:
        if line == "$ cd ..":
            dirs.append(current_dirs.pop())
        elif line.startswith("$ cd "):
            current_dirs.append(0)
        elif not line.startswith("dir ") and not line.startswith("$ ls"):
            for i, d in enumerate(current_dirs):
                current_dirs[i] += int(line.split(" ")[0])
    return current_dirs + dirs


def part_a():
    return sum(filter(lambda d: d <= 100000, parse()))


def part_b():
    dirs = parse()
    required_space = 30000000 - (70000000 - max(dirs))
    return min(filter(lambda d: d >= required_space, dirs))


if __name__ == "__main__":
    puzzle.answer_a = part_a()
    puzzle.answer_b = part_b()

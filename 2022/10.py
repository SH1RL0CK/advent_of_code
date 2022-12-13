from aocd.models import Puzzle

puzzle = Puzzle(2022, 10)
input_data = puzzle.input_data.splitlines()


def part_a():
    result = 0
    x = 1
    cycle = 0
    control_cycles = list(range(20, 221, 40))
    for line in input_data:
        line = line.split(" ")
        num = int(line[1]) if len(line) == 2 else 0
        cycles = 2 if line[0] == "addx" else 1
        for _ in range(cycles):
            cycle += 1
            if cycle in control_cycles:
                result += cycle * x
        x += num
    return result


def part_b():
    result = []
    x = 1
    cycle = -1
    current_line = ""
    for line in input_data:
        line = line.split(" ")
        num = int(line[1]) if len(line) == 2 else 0
        cycles = 2 if line[0] == "addx" else 1
        for _ in range(cycles):
            cycle += 1
            current_line += "#" if cycle in list(range(x - 1, x + 2)) else "."
            if cycle == 39:
                result.append(current_line)
                current_line = ""
                cycle = -1
        x += num
    return "\n".join(result)


if __name__ == "__main__":
    puzzle.answer_a = part_a()
    print(part_b())

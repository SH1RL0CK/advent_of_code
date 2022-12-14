from dataclasses import dataclass

from aocd.models import Puzzle

puzzle = Puzzle(2022, 11)
input_data = puzzle.input_data.split("\n\n")


@dataclass(order=True)
class Monkey:
    items: list[int]
    operation: str
    divisible_by: int
    if_true: int
    if_false: int
    inspected_items: int = 0


def parse():
    monkeys = []
    for monkey in input_data:
        monkey = monkey.splitlines()
        monkeys.append(
            Monkey(
                items=[int(i) for i in monkey[1].split(":")[1].split(", ")],
                operation=monkey[2].split("= ")[1],
                divisible_by=int(monkey[3].split("by ")[1]),
                if_true=int(monkey[4][-1]),
                if_false=int(monkey[5][-1]),
            )
        )
    return monkeys


def part_a():
    monkeys: list[Monkey] = parse()
    for round in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspected_items += 1
                old = item
                item = eval(monkey.operation) // 3
                if item % monkey.divisible_by == 0:
                    monkeys[monkey.if_true].items.append(item)
                else:
                    monkeys[monkey.if_false].items.append(item)
            monkey.items = []
        print(round)
    monkeys.sort(key=lambda m: m.inspected_items, reverse=True)
    return monkeys[0].inspected_items * monkeys[1].inspected_items


if __name__ == "__main__":
    puzzle.answer_a = part_a()

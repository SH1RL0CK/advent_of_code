from aocd.models import Puzzle

puzzle = Puzzle(2022, 8)
input_data = puzzle.input_data.splitlines()


def parse():
    return [[int(n) for n in l] for l in input_data]


def part_a():
    trees = parse()
    visible_trees = len(trees) * 2 + len(trees[0][1:-1]) * 2
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            if any(
                trees[i][j] > n
                for n in [
                    max(trees[i][j + 1 :]),
                    max(trees[i][:j]),
                    max([trees[k][j] for k in range(i + 1, len(trees))]),
                    max([trees[k][j] for k in range(i)]),
                ]
            ):
                visible_trees += 1
    return visible_trees


def part_b():
    trees = parse()
    highest_score = 0
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            tree_score = 1
            for tree_list in [
                trees[i][j + 1 :],
                list(reversed(trees[i][:j])),
                [trees[k][j] for k in range(i + 1, len(trees))],
                [trees[k][j] for k in range(i - 1, -1, -1)],
            ]:
                current_score = 0
                for tree in tree_list:
                    current_score += 1
                    if tree >= trees[i][j]:
                        break
                tree_score *= current_score
            if tree_score > highest_score:
                highest_score = tree_score
    return highest_score


if __name__ == "__main__":
    puzzle.answer_a = part_a()
    puzzle.answer_b = part_b()

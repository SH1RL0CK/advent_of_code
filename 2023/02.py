from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=2)
input_data = puzzle.input_data.splitlines()
example_input_data = puzzle.examples[0].input_data.splitlines()


def part_a():
    result = 0
    for line in input_data:
        game = line.split("Game ")[1].split(": ")
        game_id = int(game[0])
        for round in game[1].split("; "):
            if not round_is_possible(round):
                break
        else:
            result += game_id
    return result


def round_is_possible(round):
    total_clues = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for clue in round.split(", "):
        s = clue.split(" ")
        if total_clues[s[1]] < int(s[0]):
            return False
    return True


def part_b():
    result = 0
    for line in input_data:
        game = line.split("Game ")[1].split(": ")
        max_clues = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for round in game[1].split("; "):
            for clue in round.split(", "):
                s = clue.split(" ")
                if max_clues[s[1]] < int(s[0]):
                    max_clues[s[1]] = int(s[0])
        power = 1
        for value in max_clues.values():
            power *= value
        result += power
    return result


if __name__ == "__main__":
    answer_a = part_a()
    print(f"Answer A: {answer_a}")
    answer_b = part_b()
    print(f"Answer B: {answer_b}")
    puzzle.answer_a = answer_a
    puzzle.answer_b = answer_b

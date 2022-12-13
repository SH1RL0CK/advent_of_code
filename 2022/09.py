from aocd.models import Puzzle

puzzle = Puzzle(2022, 9)
input_data = puzzle.input_data.splitlines()


def part_a():
    visited_positions = set()
    head = [0, 0]
    tail = [0, 0]
    for line in input_data:
        motion = line.split(" ")
        move = [0, 0]
        match motion[0]:
            case "R":
                move = [0, 1]
            case "L":
                move = [0, -1]
            case "U":
                move = [-1, 0]
            case "D":
                move = [1, 0]
        for _ in range(int(motion[1])):
            head[0] += move[0]
            head[1] += move[1]
            if 2 in [abs(head[0] - tail[0]), abs(head[1] - tail[1])]:
                tail[0] += move[0]
                tail[1] += move[1]
                if head[0] != tail[0] and head[1] != tail[1]:
                    if move[1] == 0:
                        tail[1] = head[1]
                    else:
                        tail[0] = head[0]
            visited_positions.add((tail[0], tail[1]))
    return len(visited_positions)


if __name__ == "__main__":
    puzzle.answer_a = part_a()

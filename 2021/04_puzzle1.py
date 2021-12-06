content = open("2021/04_puzzle_input.txt", "r").read().splitlines()


numbers = content[0].split(",")

boards = []

current_board = []

for i, line in enumerate(content[2:]):
    if line != "":
        line = [x for x in line.split(" ") if x]
        current_board.append(line)
    if i == len(content[2:]) - 1 or content[2:][i + 1] == "":
        boards.append(current_board)
        current_board = []


def result(board, number):
    board_sum = 0
    for row in board:
        board_sum += sum([int(x) for x in row if x != "x"])
    return board_sum * int(number)


def winner(boards):
    for number in numbers:
        for board in boards:
            for row in board:
                for i, item in enumerate(row):
                    if number == item:
                        row[i] = "x"
                if row.count("x") == 5:
                    return result(board, number)

            for i in range(5):
                column = []
                for row in board:
                    column.append(row[i])
                if column.count("x") == 5:
                    return result(board, number)


if __name__ == "__main__":
    print(winner(boards))

import copy

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


def result(board, number_index):
    board_sum = 0
    for row in board:
        board_sum += sum([int(x) for x in row if x in numbers[number_index + 1 :]])
    return board_sum * int(numbers[number_index])


def last_winner(boards):
    winners = []
    winner = 0, 0
    boards_cpy = copy.deepcopy(boards)
    for i, number in enumerate(numbers):
        for j, board in enumerate(boards_cpy):
            for row in board:
                for k, item in enumerate(row):
                    if number == item:
                        row[k] = "x"
                if row.count("x") == 5:
                    if board not in winners:
                        winners.append(board)
                        winner = boards[j], i

            for k in range(5):
                column = []
                for row in board:
                    column.append(row[k])
                if column.count("x") == 5:
                    if board not in winners:
                        winners.append(board)
                        winner = boards[j], i
            if len(winner) == len(boards):
                return result(*winner)
    return result(*winner)


if __name__ == "__main__":
    print(last_winner(boards))

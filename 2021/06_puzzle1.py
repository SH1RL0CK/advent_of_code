content = open("2021/06_puzzle_input.txt", "r").read()

lanternfishes = list(map(int, content.split(",")))


for day in range(80):
    lanternfishes_cpy = lanternfishes.copy()
    for i, fish in enumerate(lanternfishes_cpy):
        lanternfishes[i] -= 1
        if lanternfishes[i] == -1:
            lanternfishes[i] = 6
            lanternfishes.append(8)

print(len(lanternfishes))

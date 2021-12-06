content = open("2021/06_puzzle_input.txt", "r").read()

initial_state = list(map(int, content.split(",")))

lanternfishes = [0] * 9

for fish in initial_state:
    lanternfishes[fish] += 1


for day in range(256):
    births = lanternfishes[0]
    for i, number in enumerate(lanternfishes[:-1]):
        lanternfishes[i] = lanternfishes[i + 1]
    lanternfishes[6] += births
    lanternfishes[8] = births

print(sum(lanternfishes))

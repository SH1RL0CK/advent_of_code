content = open("2021/09_puzzle_input.txt", "r").read().splitlines()

risk = 0

for i, line in enumerate(content):
    for j, elm in enumerate(line):
        if not (j > 0 and elm >= line[j - 1]) and not (j < len(line) - 1 and elm >= line[j + 1]) and not (i > 0 and elm >= content[i - 1][j]) and not (i < len(content) - 1 and elm >= content[i + 1][j]):
            risk += int(elm) + 1

print(risk)

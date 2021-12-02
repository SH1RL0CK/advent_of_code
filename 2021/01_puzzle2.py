with open("2021/01_puzzle_input.txt", "r") as file:
    content = file.readlines()

increased = 0

for i in range(len(content)):
    if i == 0:
        continue
    if len(content) < i + 3:
        break
    if (int(content[i]) + int(content[i + 1]) + int(content[i + 2])) > (int(content[i - 1]) + int(content[i]) + int(content[i + 1])):
        increased += 1

print(increased)

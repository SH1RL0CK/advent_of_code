with open("01_puzzle_input.txt", "r") as file:
    content = file.readlines()

increased = 0

for i, line in enumerate(content):
    if i == 0:
        continue
    if int(line) > int(content[i - 1]):
        increased += 1

print(increased)

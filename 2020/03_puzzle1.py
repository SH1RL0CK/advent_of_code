with open("03_input.txt") as file:
    lines = file.readlines()

position = 3
trees = 0

for line in lines[1:]:
    line = line[:-1]
    if position >= len(line):
        position -= len(line)
    if line[position] == '#':
        trees += 1
    position += 3


print(trees)
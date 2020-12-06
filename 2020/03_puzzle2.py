with open("03_input.txt") as file:
    lines = file.readlines()

def find_trees(right, down):
    position = right
    trees = 0

    for i in range(down, len(lines), down):
        line = lines[i][:-1]
        if position >= len(line):
            position -= len(line)
        if line[position] == '#':
            trees += 1
        position += right
    return trees

result = 1

for right, down in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    result *= find_trees(right, down)

print(result)
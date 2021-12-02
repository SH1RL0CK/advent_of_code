content = open("2021/02_puzzle_input.txt", "r").read().splitlines()

depth = 0
horizontal = 0

for line in content:
    if line.startswith("forward "):
        horizontal += int(line.split(" ")[1])
    elif line.startswith("down "):
        depth += int(line.split(" ")[1])
    elif line.startswith("up "):
        depth -= int(line.split(" ")[1])
print(horizontal * depth)

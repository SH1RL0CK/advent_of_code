content = open("2021/02_puzzle_input.txt", "r").read().splitlines()

depth = 0
horizontal = 0
aim = 0

for line in content:
    if line.startswith("forward "):
        value = int(line.split(" ")[1])
        horizontal += value
        depth += aim * value
    elif line.startswith("down "):
        aim += int(line.split(" ")[1])
    elif line.startswith("up "):
        aim -= int(line.split(" ")[1])
print(horizontal * depth)

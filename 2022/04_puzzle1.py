import re

content = open("2022/04_puzzle_input.txt", "r").read().split("\n\n")

stacks_start_state = content[0].splitlines()
producere = content[1].splitlines()

stacks = []

for crate in stacks_start_state[-1].split("  "):
    stacks.append([])


for line in stacks_start_state[:-1]:
    for i in range(len(stacks)):
        crate = line[1 + i * 4]
        if crate != " ":
            stacks[i].append(crate)


for line in producere:
    numbers = re.findall("[0-9]+", line)
    cranes = int(numbers[0])
    stack1 = int(numbers[1]) - 1
    stack2 = int(numbers[2]) - 1
    stacks[stack2] = [*reversed(stacks[stack1][:cranes]), *stacks[stack2]]
    stacks[stack1] = stacks[stack1][cranes:]

result = "".join([stack[0] for stack in stacks])
print(result)

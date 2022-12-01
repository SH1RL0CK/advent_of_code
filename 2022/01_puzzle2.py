content = open("2022/01_puzzle_input.txt", "r").read().split("\n\n")
elements = [e.split("\n") for e in content]

cal = []

for e in elements:
    cal.append(sum([int(c) for c in e]))

print(sum(sorted(cal)[-3:]))

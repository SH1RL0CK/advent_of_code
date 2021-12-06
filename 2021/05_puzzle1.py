# Insperation for this soltution: https://github.com/leonfroschauer

content = open("2021/05_puzzle_input.txt", "r").read().splitlines()

vents, result = set(), set()

for row in content:
    pos1, pos2 = row.split(" -> ")
    x1, y1 = pos1.split(",")
    x2, y2 = pos2.split(",")

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if (x1, y) in vents:
                result.add((x1, y))
            vents.add((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if (x, y1) in vents:
                result.add((x, y1))
            vents.add((x, y1))

print(len(result))

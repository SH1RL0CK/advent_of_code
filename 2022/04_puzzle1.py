content = open("2022/04_puzzle_input.txt", "r").read().splitlines()

result = 0

for line in content:
    ranges = line.split(",")
    range1 = [int(e) for e in ranges[0].split("-")]
    range2 = [int(e) for e in ranges[1].split("-")]
    if (range1[0] >= range2[0] and range1[1] <= range2[1]) or (range2[0] >= range1[0] and range2[1] <= range1[1]):
        result += 1
print(result)

content = open("2022/04_puzzle_input.txt", "r").read().splitlines()

result = 0

for line in content:
    ranges = line.split(",")
    range1 = [int(e) for e in ranges[0].split("-")]
    range2 = [int(e) for e in ranges[1].split("-")]
    if set(range(range1[0], range1[1] + 1)).intersection(range(range2[0], range2[1] + 1)):
        result += 1
print(result)

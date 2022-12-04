import string

content = open("2022/03_puzzle_input.txt", "r").read().splitlines()

result = 0

for l in content:
    same_item = set(l[: len(l) // 2]).intersection(l[len(l) // 2 :])
    result += string.ascii_letters.find(list(same_item)[0]) + 1

print(result)

import string

content = open("2022/03_puzzle_input.txt", "r").read().splitlines()

result = 0

for i in range(0, len(content), 3):
    same_item = set(content[i]).intersection(content[i + 1], content[i + 2])
    result += string.ascii_letters.find(list(same_item)[0]) + 1

print(result)

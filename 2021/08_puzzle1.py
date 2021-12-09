content = open("2021/08_puzzle_input.txt", "r").read().splitlines()

unique_digits = 0

for line in content:
    output = line.split(" | ")[1].split(" ")
    for digit in output:
        if len(digit) in [2, 3, 4, 7]:
            unique_digits += 1

print(unique_digits)

content = open("2021/03_puzzle_input.txt", "r").read().splitlines()

gamma_rate = ""
epsilon_rate = ""

for i in range(len(content[0])):
    zeros = 0
    ones = 0
    for line in content:
        if line[i] == "0":
            zeros += 1
        else:
            ones += 1
    if ones > zeros:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

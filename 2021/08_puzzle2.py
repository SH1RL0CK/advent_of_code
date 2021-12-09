content = open("2021/08_puzzle_input.txt", "r").read().splitlines()

result = 0

for line in content:
    line = line.split(" | ")
    digits = []
    for i in range(10):
        digits.append(set())
    digit_input = sorted(line[0].split(" "), key=len)
    digits[1] = set(digit_input[0])
    digits[7] = set(digit_input[1])
    digits[4] = set(digit_input[2])
    digits[8] = set(digit_input[9])
    for digit in digit_input[6:9]:
        if all(c in digit for c in digits[4]):
            digits[9] = set(digit)
        elif all(c in digit for c in digits[7]):
            digits[0] = set(digit)
        else:
            digits[6] = set(digit)
    for digit in digit_input[3:6]:
        if all(c in digit for c in digits[1]):
            digits[3] = set(digit)
        elif all(c in digits[6] for c in digit):
            digits[5] = set(digit)
        else:
            digits[2] = set(digit)

    line_result = ""
    for digit in line[1].split(" "):
        for i, d in enumerate(digits):
            if d == set(digit):
                line_result += str(i)

    result += int(line_result)

print(result)

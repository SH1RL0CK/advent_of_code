with open('04_input.txt', 'r') as file:
    content = file.read().split("\n\n")

valid = 0
for line in content:
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if not field in line:
            break
    else:
        valid += 1

print(valid)

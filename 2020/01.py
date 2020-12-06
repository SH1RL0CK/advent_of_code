from typing import List

with open('01_input.txt', 'r') as file:
    numbers: List[int] = list(map(int, file.readlines()))

solution1: int = 0
solution2: int = 0

for num1 in numbers:
    for num2 in numbers:
        if num1 + num2 == 2020:
            solution1 = num1 * num2
        else:
            for num3 in numbers:
                if num1 + num2 + num3 == 2020:
                    solution2 = num1 * num2 * num3

print((f'puzzle1: {solution1}', f'puzzle2: {solution2}'))

#Oneliner:
print(tuple(sorted({el for el in [f'puzzle1: {num1 * num2}' if num1 + num2 == 2020 else f'puzzle2: {num1 * num2 * num3}' if num1 + num2 + num3 == 2020 else None for num1 in numbers for num2 in numbers for num3 in numbers] if el != None})))
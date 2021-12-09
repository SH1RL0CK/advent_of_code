content = open("2021/07_puzzle_input.txt", "r").read()
crabs = list(map(int, content.split(",")))

lowest_fuel = None

for i in range(1, max(crabs)):
    current_fuel = 0
    for crab in crabs:
        current_fuel += abs(crab - i)
    if lowest_fuel is None or current_fuel < lowest_fuel:
        lowest_fuel = current_fuel

print(lowest_fuel)

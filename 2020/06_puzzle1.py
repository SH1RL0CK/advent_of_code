with open('06_input.txt', 'r') as file:
    groups = file.read().split('\n\n')

result = 0
for group in groups:
    result += len(set(group.replace('\n', '')))

print(result)
with open('06_input.txt', 'r') as file:
    groups = [group.split('\n') for group in file.read().split('\n\n')]

result = 0
for group_answers in groups:
    same_answers = set(group_answers[0])
    for answer in group_answers[1:]:
        same_answers &= set(answer)
    result += len(same_answers) 

print(result)
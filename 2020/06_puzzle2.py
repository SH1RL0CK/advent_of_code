with open('06_input.txt', 'r') as file:
    groups = file.read().split('\n\n')

result = 0
for group in groups:
    group_answers = group.split('\n')
    same_answers = set(group_answers[0])
    for answer in group_answers[1:]:
        same_answers &= set(answer)
    result += len(same_answers) 

print(result)
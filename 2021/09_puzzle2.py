content = open("2021/09_puzzle_input.txt", "r").read().splitlines()

result = []

visited_fields = []


def calculate_baseline(line_number, char_number, size):
    if content[line_number][char_number] != "9" and (line_number, char_number) not in visited_fields:
        size += 1
        visited_fields.append((line_number, char_number))
        if line_number > 0:
            size = calculate_baseline(line_number - 1, char_number, size)
        if line_number < len(content) - 1:
            size = calculate_baseline(line_number + 1, char_number, size)
        if char_number > 0:
            size = calculate_baseline(line_number, char_number - 1, size)
        if char_number < len(content[line_number]) - 1:
            size = calculate_baseline(line_number, char_number + 1, size)
    return size


for i, line in enumerate(content):
    for j, elm in enumerate(line):
        if not (j > 0 and elm >= line[j - 1]) and not (j < len(line) - 1 and elm >= line[j + 1]) and not (i > 0 and elm >= content[i - 1][j]) and not (i < len(content) - 1 and elm >= content[i + 1][j]):
            result.append(calculate_baseline(i, j, 0))

result = sorted(result)

print(result[-3] * result[-2] * result[-1])

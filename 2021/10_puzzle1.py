content = open("2021/10_puzzle_input.txt", "r").read().splitlines()

points = 0

for line in content:
    open_chunks = []
    for x in line:
        if x == ")":
            if len(open_chunks) > 0 and open_chunks[-1] == "(":
                open_chunks = open_chunks[:-1]
            else:
                points += 3
                break
        elif x == "]":
            if len(open_chunks) > 0 and open_chunks[-1] == "[":
                open_chunks = open_chunks[:-1]
            else:
                points += 57
                break
        elif x == "}":
            if len(open_chunks) > 0 and open_chunks[-1] == "{":
                open_chunks = open_chunks[:-1]
            else:
                points += 1197
                break
        elif x == ">":
            if len(open_chunks) > 0 and open_chunks[-1] == "<":
                open_chunks = open_chunks[:-1]
            else:
                points += 25137
                break
        else:
            open_chunks.append(x)

print(points)

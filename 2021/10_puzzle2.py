content = open("2021/10_puzzle_input.txt", "r").read().splitlines()

points = []


def line_is_incomplete(line):
    open_chunks = []
    for x in line:
        if x == ")":
            if len(open_chunks) > 0 and open_chunks[-1] == "(":
                open_chunks = open_chunks[:-1]
            else:
                return False, []
        elif x == "]":
            if len(open_chunks) > 0 and open_chunks[-1] == "[":
                open_chunks = open_chunks[:-1]
            else:
                return False, []
        elif x == "}":
            if len(open_chunks) > 0 and open_chunks[-1] == "{":
                open_chunks = open_chunks[:-1]
            else:
                return False, []
        elif x == ">":
            if len(open_chunks) > 0 and open_chunks[-1] == "<":
                open_chunks = open_chunks[:-1]
            else:
                return False, []
        else:
            open_chunks.append(x)
    return True, open_chunks


for line in content:
    incomplete, open_chunks = line_is_incomplete(line)
    open_chunks.reverse()
    if incomplete:
        line_points = 0
        for x in open_chunks:
            line_points *= 5
            for i, c in enumerate(["(", "[", "{", "<"]):
                if x == c:
                    line_points += i + 1
        points.append(line_points)

points = sorted(points)
print(points[len(points) // 2])

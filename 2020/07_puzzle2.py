'''solution by https://github.com/Defelo''' 
import re
bags = open('07_input.txt', 'r').read().splitlines()

g = {}
for line in bags:
    a = re.match(r"^([a-z]+ [a-z]+) bags", line).group(1)

    b = re.findall(r"(\d+) ([a-z]+ [a-z]+) bags?", line)
    g.setdefault(a, []).extend(b)
cnt = -1
q = [(1, "shiny gold")]
while q:
    n, p = q.pop(0)
    
    cnt += n
    q += [(n * int(a), b) for a, b in g.get(p, [])]
print(cnt)
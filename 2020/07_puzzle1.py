'''solution by https://github.com/Defelo''' 
import re
bags = open('07_input.txt', 'r').read().splitlines()

g = {}
for line in bags:
    a, *b = re.findall(r'([a-z]+ [a-z]+) bags?', line)
    for x in b:
        g.setdefault(x, []).append(a)

cnt = -1
q = ["shiny gold"]
visited = set()
while q:
    p = q.pop(0)
    if p in visited:
        continue
    visited.add(p)
    
    cnt += 1
    q += g.get(p, [])

print(cnt)




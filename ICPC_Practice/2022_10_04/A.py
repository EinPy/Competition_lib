import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



s = INP()
start = s[-1]
pos = []
starts = {}
n = ni()
for _ in range(n):
    a = INP()
    if a[0] not in starts:
        starts[a[0]] = 1
    else:
        starts[a[0]] += 1
    pos.append(a)
    
if start not in starts:
    print("?")
    
found = False
for j in range(n):
    if pos[j][0] == start:
        if pos[j][-1] not in starts or (pos[j][-1] in starts and starts[pos[j][-1]] == 1 and pos[j][-1] == pos[j][0]):
            print(f'{pos[j]}!')
            found = True
            break

if not found:
    for j in range(n):
        if pos[j][0] == start:
            print(pos[j])
            break
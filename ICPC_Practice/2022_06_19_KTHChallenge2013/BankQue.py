import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,t,p,d):
    p.sort()
    p = p[::-1]
    use = 0
    print(p)
    for i in range(t):
        if i in d:
            print(d[t])

    
    



n, t = nl()
p = []
d = {}
for i in range(n):
    c,t = nl()
    p.append((c,t))
    if t not in d:
        d[t] = [c]
    else:
        d[t].append(c)
solve(n,t,p,d)
print(d)
#print(p)
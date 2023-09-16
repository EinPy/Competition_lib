import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



a = nl()
t = nl()
i = nl()
t.sort()
i.sort()
#print(t, i)

idx = 0
cnt = 0
for time in t:
    if idx < len(i):
        while idx < len(i) and time> i[idx]:
            idx += 1
        if idx < len(i) and time <= i[idx]:
            cnt += 1
            idx += 1
    
print(cnt)
        
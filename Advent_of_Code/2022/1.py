import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


cur = 0
m = 0
b =[]
while True:
    try:
        l = INP()
        if l == "":
            b.append(cur)
            cur = 0
        else:
            cal = int(l)
            cur += cal
            m = max(m, cur)
    except:
        b.append(cur)
        break
print(m)
#print(b)
b.sort(reverse=True)
print(sum(b[:3]))

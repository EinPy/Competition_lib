import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n, d = nl()
frogs = []
for _ in range(n):
    l,w,h = nl()
    frogs.append((w,h,l))

frogs.sort()

tot = 0
stairs = [(10,5),()]
while frogs:
    w,h,l = frogs.pop()
    


print(frogs)


import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



a = ni()
b = nl()
b.sort(reverse=True)
tot = 0
#print(b)
for i in range(len(b)):
    if (i+1)%3 == 0:
        #print(i)
        tot += b[i]
print(tot)
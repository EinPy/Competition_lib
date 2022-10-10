import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
a = list(map(int,list(INP())))
#print(a)
drink = 0
cur = 0
for l in a:
#    print(cur, drink, l)
    if l == 1:
        drink += 1
        cur = 2
    else:
        if cur > 0:
            cur -= 1
            drink += 1
#    print(cur, drink, l)
#    print()

print(drink)
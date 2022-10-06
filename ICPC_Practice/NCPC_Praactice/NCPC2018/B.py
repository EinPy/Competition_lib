import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n = ni()
a = INP().split()
possible = True
c = 1
for el in a:
    try:
        num = int(el)
        if num != c:
            possible = False
    except:
        pass
    c += 1
if not possible:
    print("something is fishy")
else:
    print("makes sense")
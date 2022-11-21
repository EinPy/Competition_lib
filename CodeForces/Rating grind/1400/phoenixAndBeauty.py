import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


# 4 3
# 1 4 2 1
def solve(n,k,a):
    d = defaultdict(lambda:0)
    for el in a:
        d[el] += 1
    if len(d.keys()) > k:
        print(-1)
        return
    
    out = list(d.keys())
    out.sort()
    if len(out) < k:
        toAdd = k - len(out)
        check = 1
        while toAdd:
            if check not in out:
                out.append(check)
                toAdd -= 1
            check += 1
    out.sort()
    out = out * n
    print(len(out))
    print(" ".join(map(str,out)))

t = ni()
for case in range(t):
    n,k = nl()
    a = nl()
    solve(n,k,a)
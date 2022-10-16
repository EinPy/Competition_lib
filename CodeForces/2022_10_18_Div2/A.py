import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a,s):
    d = {}
    s = list(s)
   #print(n, a, s)
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = s[i]
        if a[i] in d and d[a[i]] != s[i]:
            return False
    ##print(d)
    return True


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    s = INP()
    if(solve(n,a,s)):
        print("YES")
    else:
        print("NO")
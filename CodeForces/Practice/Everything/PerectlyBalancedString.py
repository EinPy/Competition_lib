import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(s):
    n = len(s)
    charSet = set(())
    
    pos = 0
    for pos in range(n):
        if s[pos] not in charSet:
            charSet.add(s[pos])
            if pos == n-1:
                return "YES"
        else:
            break
    
    for i in range(pos, n):
        if s[i] != s[i-pos]:
            return "NO"

    return "YES"


t = ni()
for case in range(t):
    s = INP()
    print(solve(s))
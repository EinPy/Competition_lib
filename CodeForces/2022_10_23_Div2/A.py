import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve():
    n = ni()
    s = list(INP())
    a, q = 0, 0
    for i in range(n-1, -1, -1):
        #print(n, i, s)
        if s[i] == 'Q':
            a -= 1
            if a <0:
                print("No")
                return
        else:
            a += 1
    print("Yes")
    return


t = ni()
for case in range(t):
    solve()
            
            
        
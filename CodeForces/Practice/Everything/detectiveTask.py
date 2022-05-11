import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def solve(s):
    n = len(s)
    if n == 1:
        print("1")
        return
    
    l, r = -1, -1
    for i in range(n):
        if s[i] == '1':
            l = i
        if s[i] == '0':
            r = i
            break
    #print(l, r)
    if l == -1:
        l = 0
    if r == -1:
        r = n-1
    
    print(r-l+1)
        
                
t = ni()
for case in range(t):
    s = INP()
    #print(s)
    solve(s)
    #print()
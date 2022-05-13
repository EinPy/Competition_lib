import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(s):
    a = 'abcdefghijklmnopqrstuvwxyz'
    n = len(s)
    if n == 1:
        return f"Bob {a.find(s) +1}"
    
    if n % 2 != 0:
        f, l = a.find(s[0])+1, a.find(s[-1])+1
        #print(f, l)
        score = 0
        if f > l:
            for i in range(n-1):
                score += a.find(s[i]) + 1
            return f"Alice {score-l}"
        else:
            for i in range(1, n):
                score += a.find(s[i]) + 1
            return f"Alice {score-f}"
        
    score = 0
    for i in range(n):
        score += a.find(s[i]) +1
    return f"Alice {score}"
        

t = ni()
for case in range(t):
    s = INP()
    print(solve(s))
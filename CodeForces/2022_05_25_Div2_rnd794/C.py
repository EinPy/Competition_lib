import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    if n % 2 != 0:
        return "NO"
    a.sort()
    if len(set(a)) == 1:
        return "NO"
    
    pos = n-1
    out = [-1 for _ in range(n)]
    for i in range(n-1, -1, -2):
        out[i] = a[pos]
        pos -= 1
    #print(pos)
        
    for i in range(n-2, -1, -2):
        next = i -1
        #print(i)
        if out[next] > a[pos] and out[i+1] > a[pos]:  
            out[i] = a[pos]
            pos -= 1
        else:
            return "NO"
    return "YES \n" + " ".join(list(map(str,out)))
        


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))
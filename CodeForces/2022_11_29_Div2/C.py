import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n, x):
    #print()
    out = []
    out.append(x)
    mid = [ i for i in range(2,n)]
    out += mid
    out.append(1)
    if n % x != 0:
        print(-1)
        return
    if x == n:
        print(*out)
        return
    out[x-1] = n
    #print(out)
    #now make it lexographiically smaller by shifting
    #n backwards
    x -= 1
    for i in range(1, n-1):
        #print(i, x, out[x], out[i])
        if out[x] % (i+1) == 0 and out[i] % (x + 1) == 0:
            out[i],out[x] = out[x], out[i]
            x = i
    print(*out)
        
        
    
t = ni()
for case in range(t):
    n, x = nl()
    solve(n, x)
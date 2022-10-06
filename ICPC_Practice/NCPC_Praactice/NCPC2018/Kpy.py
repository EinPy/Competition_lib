import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



node, color = nl()
#each leaf is either the only one in it's color, or not
mem = [[-1 for _ in range(color+1)] for _ in range(node+1)]

def rec(n, k):
    #only with it's color
    #for a leaf v
    if n == k and n == 1:
        return 1
    if k == 2:
        return 2
    if mem[n][k] != -1:
        return mem[n][k] % (1e9 + 7)
    
    if n == k and n > 0:
        s = 1
        for i in range(1,n+1):
            s = (s * i) % (1e9 + 7)
        return s

    
    mem[n][k] = (k * rec(n-1,k-1)) % (1e9 + 7) + ((k-1)*rec(n-1, k)) % (1e9 + 7)
    return mem[n][k] % (1e9 + 7)

print(int(rec(node, color)))
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



node, color = nl()
#each leaf is either the only one in it's color, or not
mem = [[0 for _ in range(color+1)] for _ in range(node+1)]
for i in range(1,node+1):
    mem[i][2] = 2
    
    
mem[1][1] = 1
# diagonal is factorial
for i in range(2, color + 1):
    mem[i][i] = mem[i-1][i-1] * i % (1e9+7)
    

for k in range(3, color+1):
    for n in range(3,node+1):
        mem[n][k] = (k * mem[n-1][k-1] + (k-1) * mem[n-1][k]) % (1e9+7)
# Recursive case


print(int(mem[node][color]))
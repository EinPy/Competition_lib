import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(N, M):
    sums = [0] * (N + M + 1)
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            sums[i + j] += 1
    
    freq = 0
    best = []
    for i in range(1, N + M + 1):
        if sums[i] > freq:
            freq = sums[i]
            best = [i]
        elif sums[i] == freq:
            best.append(i)
    
    return best 
            
            


N, M = nl()

print('\n'.join(map(str, solve(N, M))))
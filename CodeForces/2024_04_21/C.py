import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


t = ni()
for case in range(t):
    #set all colums to the the same permutation
    #set all rows below half to be the same permutation
    n = ni()
    out = [[0 for _ in range(n)] for _ in range(n)]
    
    tot = 0
    for i in range(1, n+1):
        tot += i * ( 2 * i - 1)
    print(int(tot), 2 * n)
    
    p1 = [i + 1 for i in range(n)]
    p1 =' '.join(map(str,p1))
    p2 = [n - i for i in range(n)]
    p2 = ' '.join(map(str,p2))
    
    for op in range(n):
        #set row
        #col = op
         
        print(2, op + 1, p1)
        for row in range(n):
            out[row][op] = row + 1
            
        #set last row reversed
        print(1, n - op, p2)
        for col in range(n):
            out[n - 1 - op][col] = n - col
    
    
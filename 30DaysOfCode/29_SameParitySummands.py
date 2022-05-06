import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n,k):
    #use odd numbers
    oddN = n - (k-1)
    #use even numbers
    evenN = n - 2*(k-1)
    if oddN % 2 == 0 and evenN % 2 == 1:
        return "NO"
    
    if oddN % 2 == 1 and oddN > 0:
        return "YES\n" + " ".join(["1"]*(k-1) + [str(oddN)])
    if evenN % 2 == 0  and evenN > 0:
        return "YES\n" +" ".join(["2"]*(k-1) + [str(evenN)])
    
    return "NO"



t = ni()
for case in range(t):
    n, k = nl()
    print(solve(n,k))
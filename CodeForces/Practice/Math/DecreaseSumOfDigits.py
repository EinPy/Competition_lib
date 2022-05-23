import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def lst (s):
    return list(map(int,list(str(s))))

def solve(n,s):
    #print(n)
    if sum(lst(n)) <= s:
        return 0

    ops = 0
    for i in range(len(str(n))):
        dig = (n // (10**i)) % 10
        #print(dig)
        add = (10**i) * (10-dig)
        n += add
        ops += add
        #print(n)
        if sum(lst(n)) <= s:
            break

    return ops

    
        


t = ni()
for case in range(t):
    n, s = nl()
    print(solve(n,s))
    #print()
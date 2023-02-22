import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def gcd(a, b):
    return b if a%b == 0 else gcd(b, a% b)

def solve(n,a):
    #all multiples of the lowest possible number that can be created
    bigN = max(a)
    curG = bigN
    for num in a:
        curG = gcd(max(num, curG), min(num, curG))
    bigN = max(a)
    print(bigN // curG)
        


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
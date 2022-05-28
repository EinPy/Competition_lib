import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def solve(s):
    smiles = [";)", ":)", ":-)", ";-)"]
    n = len(s)
    for i in range(n-1):
        if s[i:i+2] in smiles:
            print(i)
        if i < n-2:
            if s[i:i+3] in smiles:
                print(i)

s = INP()
#print(s)
#print(s[0:2])
solve(s)

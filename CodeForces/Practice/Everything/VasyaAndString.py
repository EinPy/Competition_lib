from string import ascii_lowercase
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,k,a):
    alph = ascii_lowercase
    cnt = [0] * len(alph)
    changes = 0
    l, r = 0
    cnt[alph.index(a[l])] += 1
    while r < n:
        d = r - l + 1


        



n, k = nl()
a = INP()
solve(n,k,a)
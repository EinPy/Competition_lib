from string import ascii_lowercase
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,k,a):
    if n == 1:
        print(1)
        return
    alph = ascii_lowercase
    cnt = [0] * (len(alph) + 1)
    changes = 0
    l, r = 0, 0
    d = 0
    cnt[alph.index(a[l])] += 1
    while r < n-1:
        r += 1
        cnt[alph.index(a[r])] += 1
        if sum(cnt) - max(cnt) > k:
            cnt[alph.index(a[l])] -= 1
            l += 1
        d = max(d, r - l + 1)
    print(d)
        


        



n, k = nl()
a = INP()
solve(n,k,a)
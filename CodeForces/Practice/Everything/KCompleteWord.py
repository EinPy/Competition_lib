from string import ascii_lowercase
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,k,s):
    alph = ascii_lowercase
    cnt = [[0 for _ in range(26)] for j in range((k+1)//2)]
    for i in range(n):
        cnt[min(i%k, k - i% k - 1)][alph.index(s[i])] += 1

    ans = 0
    for i in range(k // 2):
        ans += 2 * n // k - max(cnt[i])
    if k % 2 == 1:
        ans += n // k - max(cnt[k//2])
    
    print(ans)


t = ni()
for case in range(t):
    n ,k = nl()
    s = INP()
    solve(n,k,s)
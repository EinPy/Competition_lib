from string import ascii_lowercase
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n, k, s):
    alph = ascii_lowercase
    cnt = [[0 for _ in range(k)] for _ in range(len(alph))]
    
    for i in range(0, k * (n // k), k):
        for j in range(i, i + k):
            cnt[alph.index(s[j])][j%k] += 1
            print(s[j], j%k, alph.index(s[j]))
            
    for line in cnt: print(line)
        


t = ni()
for case in range(t):
    n, k = nl()
    s = INP()
    solve(n, k, s)
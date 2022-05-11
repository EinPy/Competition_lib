#To start code
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#code


#A, B, C, D, E, F, G, H, I, J, K,
#  L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.


def solve(n,m,a):
    alph = "abcdefghijklmnopqrstuvwxyz"
    best, cur = 1e5, 1e5
    for i in range(n-1):
        for j in range(i+1, n):
            score = 0
            for c in range(m):
                score += abs(alph.find(a[i][c]) - alph.find(a[j][c]))
            best = min(best, score)
    return best




t = ni()
for case in range(t):
    n, m = nl()
    a = []
    for i in range(n):
        a.append(INP())
    print(solve(n,m,a))
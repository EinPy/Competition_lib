import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    #convert to int
    col = ord(a[1]) - ord('a')
    out = []
    for i in range( 1, 9):
        if i != int(a[1]):
            out.append(f"{a[0]}{i}")
    for i in range(8):
        if chr(ord('a') +i) != a[0]:
            out.append(f"{chr(ord('a') +i)}{a[1]}")
    print('\n'.join(out))


t = ni()
for case in range(t):
    n = 1
    a = INP()
    solve(n,a)
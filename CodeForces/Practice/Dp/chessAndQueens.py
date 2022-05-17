https://cses.fi/problemset/task/1624
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(arr):
    d1 = [0] * 15
    d2 = [0] * 15
    c = [0] * 8
    ans = 0
    
    def dfs(r): #place queen in row r
        if r == 8:
            ans += 1
        else:
            for i in range(8):
                if arr[r][i] == '*':
                    continue
                

t = 8
arr = []
for case in range(t):
    a = nl()
    arr.append(a)
    solve(arr)
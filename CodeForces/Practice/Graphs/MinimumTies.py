#https://codeforces.com/problemset/problem/1487/C
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n):
    # all teamps play n-1 matches
    #max points is 3(n-1)
    #min points is 0
    
    #if two, one tie
    #if three, 1 -1 1
    #if n is odd the problem is quite simple as each team 
    #can lose and win an even number of mathces
    winCnt = [0 for _ in range(n)]
    if n % 2 != 0:
        for i in range(n):
            for j in range(i,n):
                if winCnt[i] < n / 2:
                    print(1, end = " ")
                    winCnt[i] += 1
                else:
                    print(0, end = " ")
                    winCnt[j] += 1
            
    


t = ni()
for case in range(t):
    n = ni()
    solve(n)
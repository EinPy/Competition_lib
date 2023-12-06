import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    #if the array is already sorted from some starting index in some direction
    #check forwards and backwards and identify the break
    #forwards
    br = 0
    bridx = 0
    possible = True
    for i in range(n-1):
        if a[i+1] >= a[i]:
            #ok
            continue
        else:
            if br == 0:
                br = 1
                bridx = i+1
            else:
                possible = False
    if possible:
        if 

        


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    a1, b1, a2, b2, a3, b3 = a
    
    A1, A2, A3 = a1*b1, a2*b2, a3*b3
    arr = [[A1, a1, b1], [A2, a2, b2], [A3, a3, b3]]
    arr.sort(reverse= True)
    #always place the first rectangle first
    #four ways to place the second rectangel
    for i in range(4):
        if i<= 1:
            
    area, x, y = arr[0]
    #case 1
    
            
    


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
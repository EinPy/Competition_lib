import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



r, c, a = nl()
b = r*c - a

def solve():
    if r == 1 or c == 1:
        print(1)
        return
            
    
    #there will always be a maximum of two splits to achieve a or b, but can be less
    #can check all cases and then take best?
    if a % r == 0:
        print(1)
        return
    if a % c == 0:
        print(1)
        return 
    for i in range(1,c+1):
        if a % i == 0 and a // i <= r:
            print(2)
            return
        if b % i == 0 and b // i <= r:
            print(2)
            return
    for i in range(1,r+1):
        if a % i == 0 and a // i <= c:
            print(2)
            return
        if b % i == 0 and b // i <= c:
            print(2)
            return
    print(3)
    return
solve()
        

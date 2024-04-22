import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    #first check if array is beautiful
    #the entire array must consists of the outer numbers 
    #how fast can you make the outer numbers be different
    #or, make not every other number be the outer number, 2 ways
    
    n = len(a)
    if len(set(a)) == 1:
        print(-1)
        return
    
    #check if there are different numbers on two sides of a 
    targ = a[0]

    #otherwise find shortest distance to either first number, last number
    #or between two different numbers
    first = 0
    while a[first] == targ:
        first += 1
    last= n-1
    while a[last] == targ:
        last -= 1
        
    #find diff between two numbers
    
    best= 10000000000
    cur = 0
    s = False
    for i in range(n):
        if a[i] != targ:
            p1 = i+1
            while p1 < n and a[p1] == targ:
                p1 += 1
            best = min(best, p1 - i)
    #print('last', last, a)
    #print([first, n - (last+1), best])
    print(min([first, n - (last+1), best-1]))
    
t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
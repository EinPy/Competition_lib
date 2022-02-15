import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def solve(n,a):
    
    ev = False
    odd = False
    curMax = 0
    #array with all numbers currently larger than than that number are even?
    #True if all greater are even, False if all greater are odd
    curMax = 0
    allEven = [True for _ in range(n)]
    for i, v in enumerate(a):
        if v < curMax:
            if v
        if v % 2 == 0:
            allEven[v] = True
        else:
            allEven[v] = False
            
        curMax = max(curMax,v)
            
        
        
        

T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    solve(n,a)
    
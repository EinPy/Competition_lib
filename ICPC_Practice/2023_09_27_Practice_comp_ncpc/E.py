import sys, math
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(l, m, lawnmowers):
    best_price = 9*10**9
    result = []
    for i in range(m):
        n, p, c, t, r = lawnmowers[i]
        k = l / (c * t)
        check = True
        if k > math.floor(k):
            if 10080 < k*t+math.floor(k)*r:
                check = False
        else:
            if 10080 < k*(r+t):
                check = False 
        
        if check and p < best_price:
            best_price = p
            result = [n]
        elif check and p == best_price:
            best_price = p
            result.append(n)
    
    return result

def main():
    l, m = nl()
    lawnmowers = []
    
    for _ in range(m):
        n, p, c, t, r = list(INP().split(','))
        lawnmowers.append([n, int(p), int(c), int(t), int(r)])
    
    res = solve(l, m, lawnmowers)
    if len(res) == 0:
        print("no such mower")
    else:
        print('\n'.join(res))

if __name__ == '__main__':
    main()
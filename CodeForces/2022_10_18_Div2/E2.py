import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




def s(a,b,c,d):
    div = a * b
    # for a multiple of div, find 
    biggest = c * d
    #inisight:
    # x * y must be at least twice a * b
    # must have same parity (odd even)
    #if the double exists, it is divisible?
    testfor = True # for A
    if d - c < b -a:
        testfor = False
    
    
    
    if 2 * a <= d and 2 * a > b and 2 * a <= c:
        if (4 * (a*a)) // div == (4 * (a*a)) / div:
            print(2 *a, 2 * a)
            return
    if 2 * b <= c and 2 * b > a and 2 * b <= d:
        if (4 * (b*b)) // div == (4 * (b*b)) / div:
            print(2 *b, 2 * b)
            return
    if 2 * a <= c and 2 * b <= d:
        if (4 * a * b) // div == (4 * a * b) / div:
            print(2*a, 2*b)
            return
    for i in range(100000):
        targ = i * div
        if targ > biggest:
            break
        if targ < (a * b):
            continue
        else:
            if testfor:
                for x in range(c, a, -1):
                    if targ // x == targ / x and targ // x > b and targ // x <= d:
                        print(x, targ//x)
                        return
            else: 
                for y in range(d, b, -1):
                    if targ // y == targ / y  and targ // y > a and targ// y <= c:
                        #print( targ // y == targ /y)
                        print(targ // y, y)
                        return
        #create this number within boundries
    print(-1 ,-1)
    return
        
t = ni()
for case in range(t):
    a, b, c, d = nl()
    s(a,b,c,d)

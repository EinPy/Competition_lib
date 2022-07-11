import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a,b):
    odd = []
    for num in a:
        if num % 2 == 1:
            if num != 1:
                odd.append(num)
    odd.sort()
    b.sort()
    odd.reverse()
    b.reverse()
    #print(odd, b)
    possible = False
    for num in odd:
        for i in range(len(b)):
            c = b[i]
            if num == c:
                b.pop(i)
                possible = True
                break
            rebreak = False
            while c > num:
                c = c//2
                if c == num:
                    b.pop(i)
                    possible = True
                    rebreak = True
                    break
            if rebreak:
                break
        if possible == False:
            return "NO"
    return "YES"

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    b = nl()
    print(solve(n,a,b))
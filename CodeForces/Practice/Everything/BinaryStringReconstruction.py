import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n0,n1,n2):
    s = ''
    if n1 == 0:
        if n0:
            return '0' * (n0 + 1)
        return '1' * (n2 + 1)

    if n2 != 0:
        s += '1' * (n2 + 1)

    if n2:
        for _ in range(n1):
            if _ % 2 != 0:
                s += '1'
            else:
                s+= '0'
    else:
         if n1:
            s += '01'
            n1 -= 1
            for _ in range(n1):
                if _ % 2 != 0:
                    s += '1'
                else:
                    s+= '0'
    if s != '':
        i = s.find('0')
        s = s[:i] + '0' * n0 + s[i:]
        
    return s


t = ni()
for case in range(t):
    n0, n1, n2 = nl()
    print(solve(n0,n1,n2))

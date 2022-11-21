import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve():
    a = list(INP())
    b = INP().split()
    
    seen1 = {}
    seen2 = {}
    if len(a) != len(b):
        print('False')
        return
    else:
        for i in range(len(a)):
            if a[i].lower() in seen1:
                if b[i].lower() != seen1[a[i].lower()]:
                    print('False')
                    return
            else:
                seen1[a[i].lower()] = b[i].lower()
                
            if b[i].lower() in seen2:
                if a[i].lower() != seen2[b[i].lower()]:
                    print('False')
                    return
            else:
                seen2[b[i].lower()] = a[i].lower()
                
    print('True')

solve()
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    if n < 4:
        print(n)
        return
    ##print(a)
    counter= {}
    for num in a:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] +=1 
            
    ops = 0
    
    def check1(ops):
        triv = True
        while triv and len(a) > 3:
            for i in range(1,len(a)):
                if a[i] == a[(i+2) % len(a)]: # want to remove
                    if a[i-1] != a[(i+1) % len(a)]:
                        counter[a[i]] -= 1
                        a.pop(i)
                        ops +=1
                        break
                if i == len(a)-1:
                    triv = False
                    break
        return ops
    #if not something that is a potential threat can be removed
    #then remove the most common element
    def check2(num):
        found = False
        for i in range(len(a)):
            if a[i] == num:
                if a[i-1] != a[(i+1) % len(a)]:
                    counter[num] -= 1
                    a.pop(i)
                    found = True
                    break
        return found
    
    
    while len(a) > 3:
        #print(a)
        s0 = len(a)
        ops = check1(ops)
        if len(a) < 4:
            print(ops + len(a))
            return
        big = 0
        cur = 0
        for c in counter.keys():
            if counter[c] > cur:
                cur = counter[c]
                big = c
        if check2(big):
            ops += 1
        if len(a) < 4:
            print(ops + len(a))
            return
        if s0 == len(a):
            ops += 1
            a.pop(0)
            a.pop(0)
        
    print(len(a) + ops)


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
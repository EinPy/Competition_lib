import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    possible = True
    a.sort()
    cnt = Counter(a)
    ops = 0
    out = []
    if cnt[0] == 0:
        possible = False
        print(' '.join(map(str,[0] + [-1]*(n))))
        return 
    
    #keep track of largest numbers
    stack = []
    #print(cnt)
    #print(a)
    i = 0
    tot = 0
    for i in range(0,n+1):
        if i > 0 and cnt[i-1] == 0:
            #print(stack)
            if len(stack) == 0:
                possible = False
            else:
                big = stack.pop()
                #make the second last element
                tot += (i-1) - big
                
        if possible:
            out.append(tot + cnt[i])
        else:
            out.append(-1)
            
        if i > 0 and cnt[i-1] > 1:
            #print(i-1, cnt[i-1])
            stack += [i-1] * (cnt[i-1]-1)
            #print(stack)
            
            
    print(' '.join(map(str,out)))
    return
        

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)
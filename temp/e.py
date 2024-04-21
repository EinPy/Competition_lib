import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




n = ni()
arr = []

for _ in range(n):
    arr.append(list(map(int, list(INP()))))
    
for l in arr: print(l)

out = [[0 for _ in range(n)] for _ in range(n)]

def col(r1, c1, r2, c2):
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1 ):
            
            out[r][c] = 1

def rec(r1, c1, r2, c2):
    if r1==r2 and c1 == c2:
        #there is only one square, color it white
        out[r1][c1] = arr[r1][c1] # reduntant but included for clarity
        return
    else:
        #find the four sums i think?
        q1, q2, q3, q4 = 0,0,0,0
        sz = (r2 - r1) // 2
        for rr in range(r1, r1 + sz+1):
            for cc in range(c1, c1 + sz+1):
                #could be done with 2d prefix array but not neccesary
                q1 += arr[rr][cc]
                
        for rr in range(r1, r1+sz+1):
            for cc in range(c1 + sz+1, c2+1):
                #could be done with 2d prefix array but not neccesary
                q2 += arr[rr][cc]
        
        for rr in range(r1 + sz+1, r2+1):
            for cc in range(c1 , c1 + sz+1):
                #could be done with 2d prefix array but not neccesary
                q3 += arr[rr][cc]
                 
        for rr in range(r1 + sz+1, r2+1):
            for cc in range(c1 + sz+1, c2+1):
                #could be done with 2d prefix array but not neccesary
                q4 += arr[rr][cc]
                
        #q1
        q1c = (r1, c1, r1 + sz, c1 + sz)
        #q2
        q2c = (r1, c1 + sz+1, r1+sz, c2)
        #q3
        q3c = (r1 + sz+1, c1, r2, c1 + sz)
        #q4
        q4c = (r1 + sz+1, c1 + sz+1, r2, c2)
        
        
        mv = [(q1, q1c), (q2, q2c), (q3, q3c),(q4, q4c)]
        print(mv)
        
        mv.sort()
        
        #make blackest black
        col(*mv[-1][1])
        #print(mv)
        #recurse on two middle one
        rec(*mv[1][1])
        rec(*mv[2][1])
         
diff = 0           

rec(0,0, n- 1, n - 1)


for r in range(n):
    for c in range(n):
        if out[r][c] != arr[r][c]:
            diff += 1
print(diff)
for l in out: print ("".join(map(str,l)))
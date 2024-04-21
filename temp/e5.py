import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


from itertools import permutations


n = ni()
arr = []

for _ in range(n):
    arr.append(list(map(int, list(INP()))))
    


out = [[0 for _ in range(n)] for _ in range(n)]

def rec(r1, c1, r2, c2):
    #strucute [all 0, all 1, recurse]
    ret = [0,0,0]
    if r1 + 1 == r2:
        ret[0] = arr[r1][c1]
        ret[1] = 1 - arr[r1][c1]
        ret[2] = 0 
        out[r1][c1] = arr[r1][c1]
    else:
        sz = (r2 - r1) // 2
        r_mid = r1 + sz
        c_mid = c1 + sz
        
        #2x2 of 3 long dp arrays
        data = [
            [[0,0,0], [0,0,0]],
            [[0,0,0], [0,0,0]]
            ]
        data[0][0] = rec(r1, c1, r_mid, c_mid)
        data[1][0] = rec(r_mid, c1, r2, c_mid)
        data[0][1] = rec(r1, c_mid, r_mid, c2)
        data[1][1] = rec(r_mid, c_mid, r2, c2)
        
        # nice trick to flatten array?
        for idx in range(4):
            ret[0] += data[idx // 2][idx % 2][0]
            ret[1] += data[idx//2][idx%2][1]
            
        ret[2] = 1000000000000
        
        
        squares = [0, 1, 2, 3]
        best = [0,0,0,0]
        for perm in permutations(squares):
            #first grab all 0 then all 1 and recurse on the other two to test all combos
            val = 0
            val += data[perm[0] // 2][perm[0] % 2][0] # fill with white
            val += data[perm[1] // 2][perm[1] % 2][1] # fill with black 
            val += data[perm[2] // 2][perm[2] % 2][2] # rec
            val += data[perm[3] // 2][perm[3] % 2][2] # rec
            
            if val < ret[2]: #the value of recursion, which we have to use on the initial square
                ret[2] = val 
                best = perm 
        
        
        #after having found the best permutations
        #fill the squares that were chosen as white or black 
        #all squares will be filled as if they were optimally recursed, but after they have been 
        #filled they will need to be overwritennn!!! big insight
        for r in range(sz):
            for c in range(sz): #this the size of a quadrant
                #kind of a mathy complex way but otherwise it is a looot of code I think
                
                out[r1 + (best[0] // 2) * sz + r][c1 + (best[0] % 2) * sz + c] = 0
                
                out[r1 + (best[1] // 2) * sz + r][c1 + (best[1] % 2) * sz + c] = 1
                
    return ret

score = rec(0,0,n,n)
print(score[2])
for l in out:
    print(''.join(map(str,l)))
                            
            
            
            
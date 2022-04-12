import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code

        
def solve(n, l, out, targ):
    
    
    for pos in range(l):
        newOut = [o for o in out]
        for i in range(n):
            if newOut[i][pos] == '0':
                newOut[i][pos] == '1'
            else:
                newOut[i][pos] == '0'
                
    
def check(out, targ):
    for i in range(len(out)):
        
        

    
T = int(input())
for case in range(T):
    n, l = list(map(int,input().split()))
    out = input().split()
    targ = input().split()
    print(solve(n, l, out, targ))
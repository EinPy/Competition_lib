import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)



def solve(a,n):
    visited = {}
    targets = {}
    for i in range(1,n+1):
        targets[i] = []
    id = 0
    for num in a:
        id += 1
        while num > 0:
            if num in targets:
                targets[num].append(id)
            num  = num // 2
    
    
    used = [False for _ in range(n+1)]
    for val in range(n,0,-1):
        if targets[val] == []:
            return "NO"
        allUsed = True
        for org in targets[val]:
            if not used[org]:
                used[org] = True
                allUsed = False
                break
        if allUsed:
            return "NO"
    return "YES"
    

T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    print(solve(a,n))
    
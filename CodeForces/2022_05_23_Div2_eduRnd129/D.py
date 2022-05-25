import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def bfs(Graph, S):
    q = [S]
    dists = [-1 for _ in range(len(Graph))]
    while q:
        q2 = []
        for u in q:
            for n in Graph[u]:
                if dists[n] == -1:
                    dists[n] = dists[u] + 1
                    q2.append(n)
        q = q2

def solve(n, x):
    thing = list(map(int,list(str(x))))
    #print(x)
    cnt = Counter(thing)
    if cnt[0] + cnt[1] == len(thing):
        return -1
    
    
    def dfs(parts, num, move, mem):
        print(num)
        if len(parts) >= n:
            return move
        if num in mem:
            return mem[num]
        parts = list(set(parts))
        parts.sort(reverse = True)
        #print(parts)
        
        ans = []
        for dig in parts:
            if dig != 0 and dig != 0:
                newN = num * dig
                newP = list(map(int,list(str(newN))))
                cnt = Counter(newP)
                if cnt[0] + cnt[1] != len(newP):
                    ans.append(dfs(newP, newN, move + 1, mem))
        if ans:
            mem[num] = min(ans)
            return mem[num]
        return -1   
               
    m = [[[] for _ in range(10)] for _ in range(20)]
    for l in m:print(l)
    return dfs(thing, x, 0,m)
    

n, x = nl()
print(solve(n, x))
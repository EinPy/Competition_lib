#https://codeforces.com/problemset/problem/1263/D
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
words = []

#creating the graph
g = [[] for _ in range(ord('z')-ord('a')+1 + n)]

for i in range(ord('z')-ord('a')+1,ord('z')-ord('a')+1+ n):
    w = INP()
    for l in w:
        #print(l)
        g[ord(l) - ord('a')].append(i)
        g[i].append(ord(l) - ord('a'))
#print(g)
            
#this should builda graph of the words
#print(words)
#print(g)

vis = [False for _ in range(len(g))]
def s(i):
    vis[i] = True
    q = [i]
    while q:
        node = q.pop()
        for v in g[node]:
            if not vis[v]:
                q.append(v)
                vis[v] = True
                
cnt = 0
for i in range(ord('z')-ord('a')+1,len(g)):
    if not vis[i]:
        s(i)
        cnt += 1
        
print(cnt)
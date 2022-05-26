import contextvars
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def canConstructM(words, targ, mem):
    if mem[len(targ)] != -1: 
        return mem[len(targ)]
    if targ == "": 
        return True
    
    for w in words:
        if targ.find(w) == 0:
            suff = targ[len(w):] #suffix of the word
            if canConstructM(words, suff, mem):
                mem[len(targ)] = True
                return True
    
    mem[len(targ)] = True       
    return False

def solve(cnt, s):

    lets = ["A", "B", "AB", "BA"]
    
    def dfs(s, cnt, mem):
        #print(s, cnt, mem)
        l = len(s)
        if (l, cnt) in mem:
            return mem[(l, cnt)]
        if s == "":
            return True
        
        for i in range(4):
            #print("checking", s, i, cnt[i],lets[i])
            if cnt[i] > 0 and s.find(lets[i]) == 0:
                
                suff = s[len(lets[i]):]
                newC = list(cnt)
                newC[i] -= 1
                newC = tuple(newC)
                if dfs(suff, newC, mem):
                    mem[(l,newC)] = True
                    return True
                
        #print("not possible")
        mem[(l, cnt)] = False
        return False
        
    memo = {}
    cnt = tuple(cnt)
    return dfs(s, cnt, memo)

t = ni()
for case in range(t):
    cnt = nl()
    s = INP()
    if solve(cnt, s): print("YES")
    else: print("NO")
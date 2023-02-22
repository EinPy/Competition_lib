import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


t = ni()

must = []
#(dict, word, state)
#state is 0 if "and", 1 if "or"
imp = []
for case in range(t):
    l = INP()
    if len(l) < 4:
        must.append(l.strip())
    elif l[:3] != "if ":
        must.append(l.strip())
    else:
        l = l[3:]
        l  = l.split(" then ")
        #print(l)
        if " or " in l[0]:
            words = l[0].split(" or ")
            d = {}
            for w in words:
                w = w.strip()
                d[w] = True
            #print(d)
            imp.append([d, l[1].strip(), 1])
        else:
            words = l[0].split(" and ")
            d = {}
            for w in words:
                w = w.strip()
                d[w] = True
            #print(d)
            imp.append([d,l[1].strip(),0])

must = list(set(must))
#print(must)
#print(imp)
out = {}
added = [False for _ in range(len(must))]


while must:
    w = must.pop()
    out[w] = True
    for i in range(len(imp)):
        if w in imp[i][0]:
            if imp[i][-1] == 0:
                imp[i][0].pop(w)
                if len(imp[i][0].keys()) == 0:
                    out[imp[i][1]] = True
                    must.append(imp[i][1])
            if imp[i][-1] == 1:
                imp[i][0].pop(w)
                out[imp[i][1]] = True
                must.append(imp[i][1])

print(len(out.keys()))
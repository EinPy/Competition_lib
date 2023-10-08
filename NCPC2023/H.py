import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



d = {"Shadow" : [4, 6],
     "Gale" : [3, 5],
     "Ranger" : [2, 4],
     "Anvil" : [5, 7],
     "Vexia" : [2, 3],
     "Guardian" : [6, 8],
     "Thunderheart" : [5, 6],
     "Frostwhisper" : [1, 2],
     "Voidclaw" : [1, 3],
     "Ironwood" : [1, 3],
     "Zenith" : [6, 4],
     "Seraphina" : [1, 1]}

p1s, p2s = 0, 0
p1tot, p2tot = 0, 0
for board in range(3):
    p1 = INP().split()
    pp1, pp2 = 0,0
    p2 = INP().split()
    
    for c in p1:
        if c in d:
            pp1 += d[c][1]
            if c == "Thunderheart" and len(p1) == 5:
                pp1 += 6
            if c == "Zenith" and board == 1:
                pp1 += 5
            if c == "Seraphina":
                pp1 += len(p1) - 2
                
    for c in p2:
        if c in d:
            pp2 += d[c][1]
            if c == "Thunderheart" and len(p2) == 5:
                pp2 += 6
            if c == "Zenith" and board == 1:
                pp2 += 5
            if c == "Seraphina":
                pp2 += len(p2) - 2
    
            
    if pp1 > pp2:
        p1s += 1
    elif pp2 > pp1:
        p2s += 1
        
    p1tot += pp1
    p2tot += pp2
        
if p1s > p2s:
    print("Player 1")
elif p2s > p1s:
    print("Player 2")
else:
    if p1tot > p2tot:
        print("Player 1")
    elif p2tot > p1tot:
        print("Player 2")
    else:
        print("Tie")
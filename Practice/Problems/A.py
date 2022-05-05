import sys
from collections import *
sys.setrecursionlimit(10**5)
#itr = (line for line in sys.stdin.read().strip().split('\n'))
#INP = lambda: next(itr)
#def ni(): return int(INP())
#def nl(): return [int(_) for _ in INP().split()]

import random


for round in range(1000):
    lets = ["A", "B", "C"]
    l = random.randint(0,2)
    print(lets[l])
    
    door, b = list(input().split(" "))
    b = int(b)
    
    if b:
        print(door)
        
    else:
        pos = lets.index(door)
        for i in range(3):
            if i != l and i != pos:
                print(lets[i])
                
            
    waste = input()
    
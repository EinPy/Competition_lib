import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#from matplotlib import pyplot as plt


def solve(S):
    #start at (0,0) consturct random maze within 5*10**8
    #calculate endpoint, shift startpiont to have endpoint in (0,0)
    #start at 1, double every step? Cehck if you go left right left
    #impossible if ABA of some sort
    imposs = ["LRL", "RLR", "UDU", "DUD"]
    #can never have two repeating moves when one moves
    repeating = ["UU", "DD", "LL", "RR"]
    for r in repeating:
        if r in S:
            print("impossible")
            return
        
    if len(S) >= 3 and S[-3:] in imposs:
        print("impossible")
        return   


    S = list(S)
    #print(S)
    cords = [(0,0)]
    step = 1
    for i in range(len(S)):
        #print(step)
        if i < 2:
            x, y = cords[-1]
            if S[i] == "U":
                y += step
            if S[i] == "D":
                y -= step
            if S[i] == "L":
                x -= step
            if S[i] == "R":
                x += step
            cords.append((x, y))
            step *= 2
        else:
            go_back = False
            if S[i-2] == S[i]:
                if S[i] == "U" and S[i-1] == "D":
                    go_back = True
                if S[i] == "D" and S[i-1] == "U":
                    go_back = True
                if S[i] == "L" and S[i-1] == "R":
                    go_back = True
                if S[i] == "R" and S[i-1] == "L" :
                    go_back = True
            if go_back:
                cords.append(cords[-2])
            else:
                x, y = cords[-1]
                if S[i] == "U":
                    y += step
                if S[i] == "D":
                    y -= step
                if S[i] == "L":
                    x -= step
                if S[i] == "R":
                    x += step
                cords.append((x, y))
                step *= 2
            
    
            
    #print(cords)
    blocks =  []
    seen = {}
    for i in range(len(S)-1):
        x, y = cords[i+1]
        #print(x, y)
        if S[i] == "U":
            y += 1
        if S[i] == "D":
            y -= 1
        if S[i] == "L":
            x -= 1
        if S[i] == "R":
            x += 1
        if (x, y) not in seen:
            blocks.append((x, y))
            seen[(x, y )] = True
        
    #to end in the last coordinate we shift all points by that coordinate, -1 * (x, y)
    x_shift = -1 * cords[-1][0]
    y_shift = -1 * cords[-1][1]
    sx, sy = x_shift, y_shift
    blocks = [[x+x_shift, y+y_shift] for x, y in blocks]
    #print("block")
    #print(blocks)
    #print("output")
    print(sx, sy)
    print(len(blocks))
    
    for x, y in blocks:
        print(x, y)
        
    # x_cords = [x+x_shift for x, y in cords]
    # y_cords = [y+y_shift for x, y in cords]
    
    # block_x = [x for x, y in blocks]
    # block_y = [y for x, y in blocks]
    # plt.plot(x_cords, y_cords)
    # plt.scatter(block_x, block_y, marker='s', color = "red")
    # plt.grid()
    # plt.show()

        
                
            
    
    
S = INP()
solve(S)


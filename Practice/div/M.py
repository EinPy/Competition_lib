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
for i in range(t):
    bnum = int(INP(),8)
    bnum = bin(bnum)
    state = bnum[2:]
    if len(state) != 19:
        state = "0" * (19 - len(state)) + state
    #print(len(state))
    #board not complete
    end = state[-9:]
    n = state[0]
    start = state[1:10]
    #print(n + start + end == state)
    playedX = start
    playedO = bin(~int(playedX,2) & int(end,2))[2:]


    #print(playedX)
    #print(playedO)


    win_states = ["111000000", "000111000", "000000111",
                "100100100", "010010010", "001001001",
                "100010001", "001010100"]

    win = False
    for w in win_states:
        if int(playedX,2) & int(w,2) == int(w,2):
            print("X wins")
            win = True
            break
        if int(playedO,2) & int(w,2) == int(w,2):
            print("O wins")
            win = True
            break
    if not win:
        if end == '111111111':
            print("Cat's")
        else:
            print("In progress")
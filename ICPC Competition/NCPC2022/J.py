import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


m = ni()
x0,y0,x1,y1 = nl()

out = []
pos = [x0,y0]
end = [x1,y1]

for _ in range(m):
    nl()

def left():
    pos[0]-=1
    out.append("left")

def right():
    pos[0]+=1
    out.append("right")
    
def up():
    pos[1]+=1
    out.append("up")

def down():
    pos[1]-=1
    out.append("down")

def pushDown():
    while pos[1]>end[1]:
        down()
    while pos[1]<=30:
        up()
        
def pushUp():
    while pos[1]<end[1]:
        up()
    while pos[1]>=0:
        down()
    
def top():
    while pos[1]<=30:
        up()    

def bot():
    while pos[1]>=0:
        down()    
    
def align():
    while pos[0]<end[0]:
        right()
    while pos[0]>end[0]:
        left()
        
def pushInLeft(n):
    m = min(n,30-end[0])
    #print("Currently at ",pos," pushing left", n)
    while pos[0]<=30:
        right()
    while pos[1]>=0:
        down()
        for __ in range(m):
            left()
        for __ in range(m):
            right()

def pr(a):
    x = a[0] +1
    y = a[1] + 1
    mat = [[0 for _ in range(33)] for _ in range(33)]
    if 0 <= x and x <= 32 and 0 <= y and y <= 32:
        mat[y][x] = 1
    for l in mat:
        print(l)
    print()
    

def pushInRight(n):
    n = min(n,end[0])
    #print("Currently at ",pos," pushing right", n)
    while pos[0]>=0:
        left()
    while pos[1]>=0:
        down()
        for __ in range(n):
            right()
        for __ in range(n):
            left()
            
    


while pos[0]>=0:
    left()



up()
for _ in range(33):
    left()
down()
for _ in range(33):
    right()
    
bot()

#print("before start", pos)

for i in range(30-end[0]+2):
    #pr(pos)
    align()
#    print("before pusUp",pos)
    pushUp()
    while pos[0]>=0:
        left()
#    print("before top", pos)
    top()
 #   print("after top", pos)
    align()
   # print("before pushDown",pos)
    pushDown()
  #  print("after pushdown:", pos)
    
    pushInLeft(i+1)
    #print("now", pos)
    

for i in range(end[0]+2):
    #pr(pos)
    align()
    #print("before pusUp",pos)
    pushUp()
    while pos[0]>=0:
        left()
    top()
    align()
    #print("before pushDown",pos)
    pushDown()
    
    pushInRight(i+1)

print("\n".join(out))



        
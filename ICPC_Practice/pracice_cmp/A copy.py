from heapq import heappush, heappop
import math
n,m,p =  map(int,input().split())
b1,b2 = 100_000,1000_000_000_000
js,ts,fs = [],[],[]
for _ in range(n):
    a,b = map(int,input().split())
    js.append(a+b1+b*b1)

for _ in range(m):
    a,b = map(int,input().split())
    ts.append(a+b1+b*b1)

for _ in range(p):
    a,b = map(int,input().split())
    fs.append(a+b1+b*b1)

def hypot(t1,t2):
    return 

tot_dist = 0   
dists = []


print(js)
print(ts)


for (i,j) in enumerate(js):
    for ii,t in enumerate(ts):
        heappush(dists, math.hypot(j%b1-t%b1,j//b1-t//b1)+i*b1+ii*b2)
        print(i,ii,math.hypot((j-t)%b1,j//b1-t//b1)+i*b1+ii*b2)
        

math.hypot
dists.sort(reverse=True)
done_j = [False] * n
done_t = [False] * m
done = 0
#new_pos = []
while True:
    x=heappop(dists)
    dist, j, t = x%b1,int((x%b2)//b1),int(x//b2)
    
    while done_j[j] or done_t[t]:
        x=heappop(dists)
        dist, j, t = x%b1,int((x%b2)//b1),int(x//b2)
    print(dist,j,t,x)
    tot_dist+=dist
    done_j[j]=True
    done_t[t]=True
    done+=1 
    if done == n:
        break


#copy
dists = []

for (i,j) in enumerate(js):
    for ii,t in enumerate(fs):
        heappush(dists, math.hypot((j-t)%b1,j//b1-t//b1)+i*b1+ii*b2)
dists.sort(reverse=True)

done_j = [False] * n
done_t = [False] * p
done = 0
#print(new_pos)
while True:
    x=heappop(dists)
    dist, j, t = x%b1,int((x%b2)//b1),int(x//b2)
    
    while done_j[j] or done_t[t]:
        x=heappop(dists)
        dist, j, t = x%b1,int((x%b2)//b1),int(x//b2)
    print(dist,j,t)
    tot_dist+=dist
    done_j[j]=True
    done_t[t]=True
    done+=1
    if done == n:
        break     
print(tot_dist)
from heapq import heappush, heappop
import numpy as np
n,m,p =  map(int,input().split())

js,ts,fs = [],[],[]
for _ in range(n):
    a,b = map(int,input().split())
    js.append((a,b))

for _ in range(m):
    a,b = map(int,input().split())
    ts.append((a,b))

for _ in range(p):
    a,b = map(int,input().split())
    fs.append((a,b))

def hypot(t1,t2):
    return ((t1[0]-t2[0])**2+(t1[1]-t2[1])**2)**.5

tot_dist = 0   
dists = []

for (i,j) in enumerate(js):
    for ii,t in enumerate(ts):
        dists.append((hypot(j,t),i,ii))

dists.sort()
done_j = np.zeros(n)
done_t = np.zeros(m)
done = 0
#new_pos = []
while True:
    dist, j, t = heappop(dists)
    while done_j[j] > 0 or done_t[t]:
        dist, j, t = heappop(dists)
    #print(dist,j,t)
    done_j[j]=dist
    done_t[t]=1
    done+=1 
    if done == n:
        break


#copy
dists = []

for (i,j) in enumerate(js):
    for ii,t in enumerate(fs):
        dists.append((hypot(j,t),i,ii))
dists.sort()

done_j = np.zeros(n)
done_t = np.zeros(p)
done = 0
#new_pos = []
while True:
    dist, j, t = heappop(dists)
    while done_j[j] or done_t[t]:
        dist, j, t = heappop(dists)
    #print(dist,j,t)
    tot_dist+=dist
    done_j[j]=True
    done_t[t]=True
    done+=1
    if done == n:
        break     
print(tot_dist)
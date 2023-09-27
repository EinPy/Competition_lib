n,m,a,c,x0 = map(int,input().split())
l = [(x0*a+c)%m]
for _ in range(n-1):
    l.append((l[-1]*a+c)%m)
#l = [2,1,4,1,5]
print(l)

def f(lo,hi,mini,maxi):
    print(lo,hi,mini,maxi)
    if hi<lo or maxi<=mini:
        return 0
    mi = (lo+hi)//2
    tot = 0
    if l[mi]>mini and l[mi]<maxi:
        tot +=1
    tot += f(lo,mi-1,mini,min(maxi,l[mi]))
    tot += f(mi+1,hi,max(l[mi],mini),maxi)
    return tot

print(f(0,len(l)-1,-1,m+1))
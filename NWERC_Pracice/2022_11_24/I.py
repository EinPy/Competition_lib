c = float(input())
s=0.0
for _ in range(int(input())):
    a,b = map(float,input().split())
    s+=a*b
print(c*s)
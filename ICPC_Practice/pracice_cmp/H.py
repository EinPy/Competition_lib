a,b,c,d,e,f,g = map(int,input().split())

margin = 0
vols = []
while margin <= min(a,b)//2:
    vols.append(margin*(a-2*margin)*(b-2*margin))
    margin +=1
vols.sort(reverse = True)
print(vols)
vol1,vol2,vol3 = vols[:3]
print(vol1,vol2,vol3)



def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

# #def solve(c,d,vol1,vol2):
#     gcd_rem = 1
#     g = gcd(vol1,vol2)
#     while g!=1:
#         if vol1%vol2 == 0:
#             return(d,vol2)
#         elif vol2%vol1 ==0:
#             return(c,vol1)
        
#         vol1 = vol1//g
#         vol2 = vol2//g
#         gcd_rem = c%g
#         c = c%vol1
#         d = d%vol2
#     rem_prod = pow(vol1,-1,vol2)*((d-c))*vol1+c
#     prod = vol1*vol2
#     c = rem_prod
#     d = gcd_rem
#     vol1=prod
#     vol2 =g
#     print(c,d,vol1,vol2)
#     return (c,vol1)
def lcm(a, b):
	product = a*b
	#highest common factor == greatest common divisor
	hcf = gcd(a, b)
	return product // hcf


r1,v1 = pow(vol1,-1,vol2)*((d-c))*vol1+c, lcm(vol1,vol2)
_,ans = pow(v1,-1,vol3)*((e-r1))*v1+r1, lcm(v1,vol2)

print(ans) 

print(solve(2,15,3,5))   


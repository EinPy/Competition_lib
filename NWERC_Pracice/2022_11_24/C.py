out=[]

def dob():
    out.append("PH A")
    out.append("PH A")
    out.append("AD")
    out.append("PL A")

def add():
    out.append("PH B")
    out.append("PH A")
    out.append("AD")
    out.append("PL A")

out.append("ST B")

val = 2**8
t = int(input())
while val>t:
    val/=2
add()
while True:
    while val>t:
        val/=2

        dob()
    add()
    
    
up = [i for i in range(1, 8)]
down = [i for i in range(8, 15)]
print(up)
print(down)
print()
for m in range(7):
    f = up.pop(0)
    up.append(f)
    f = down.pop()
    down = [f] + down
    if m != 6:
        print(up)
        print(down)
        print()
    
for m in range(7):
    t1 = up[:]
    t2 = down[:]
    up[0],up[1], up[2], up[3],up[4], up[5], up[6] = t1[2], t2[2], t1[4], t2[4], t1[6],t2[6], t1[0]
    down[0], down[1], down[2], down[3], down[4], down[5], down[6] = t1[1], t2[3], t1[3], t2[5], t1[5], t2[1], t2[0]
    print(up)
    print(down)
    print()

def take_first(elem):
        return elem[0]
    def take_second(elem):
        return elem(1)
    n, d = list(map(int, input().split()))
    friends = []
    for i in range(n):
        friends.append(list(map(int, input().split())))
     
    friends.sort(key=take_first)
    m = 0
    t = friends[0][1]
    i, j = 0, 1
    if len(friends) == 1:
        print(friends[0][1])
    else:
        while True:
            if friends[j][0] - friends[i][0] >= d:
                if t  > m:
                    m = t
                i += 1
                if i == j:
                    t += friends[i][1]
                t -= friends[i - 1][1]
            else:
                if j != i:
                    t += friends[j][1]
                j += 1
     
            if j == len(friends):
                if t > m:
                    m = t
                break
        print(m)
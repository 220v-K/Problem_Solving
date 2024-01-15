N = int(input())
res = [1, 4, 9]
i = 10

while len(res) < N:
    flag = False
    for r in res:
        if (r*i) % (r+i) == 0:
            flag = True
            break
    
    if not flag:
        res.append(i)
    
    i += 1

print(*res[:N])
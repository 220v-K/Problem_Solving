n = int(input())
pList = []

for i in range(n):
    p = int(input())
    pList.append([])

    for j in range(p):
        a, b = map(str, input().split())
        a = int(a)
        pList[i].append([a, b])

for i in range(n):
    pList[i].sort(key=lambda x: x[0], reverse=True)
    print(pList[i][0][1])

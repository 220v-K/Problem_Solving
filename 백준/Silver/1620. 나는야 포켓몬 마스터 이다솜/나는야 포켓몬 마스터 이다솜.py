N, M = map(int, input().split())

d1 = dict()
d2 = dict()

for i in range(1, N+1):
    a = input()
    d1[str(i)] = a
    d2[a] = str(i)

for _ in range(M):
    a = input()
    if d1.get(a, -1) != -1:
        print(d1[a])
        continue
    else:
        print(d2[a])
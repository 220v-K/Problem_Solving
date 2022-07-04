n = int(input())
MAP = [list(input().split()) for _ in range(n)]
for i in range(n):
    MAP[i][1], MAP[i][2], MAP[i][3] = map(
        int, [MAP[i][1], MAP[i][2], MAP[i][3]])

MAP.sort(key=lambda x: (x[3], x[2], x[1]))
print(MAP[len(MAP)-1][0])
print(MAP[0][0])

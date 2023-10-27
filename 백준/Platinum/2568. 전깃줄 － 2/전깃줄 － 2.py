import bisect
from collections import deque
n = int(input())

lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))
lines = sorted(lines, key = lambda x: x[0])

res = []
index = []
for s, e in lines:
    a = bisect.bisect_left(res, e)
    if a == len(res):
        res.append(e)
    else:
        res[a] = e
        
    index.append(a)

cnt = len(res)-1
q = deque()
for i in range(len(index)-1, -1, -1):
    if index[i] == cnt:
        cnt -= 1
    else:
        q.appendleft(lines[i])

print(len(lines) - len(res))
for k in q:
    print(k[0])
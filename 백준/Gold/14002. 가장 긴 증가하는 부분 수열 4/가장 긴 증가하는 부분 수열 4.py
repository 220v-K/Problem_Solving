import bisect
from collections import deque
n = int(input())

lines = list(map(int, input().split()))

res = []
res_idx = []
for i in lines:
    a = bisect.bisect_left(res, i)
    if a == len(res):
        res.append(i)
    else:
        res[a] = i
        
    # 원소가 res 배열에 들어가는 index 저장.
    res_idx.append(a)

cnt = len(res)-1
q = deque()
# index 배열을 거꾸로 순회하며, 3인 원소를 찾고, 3인 원소 전에 있는 2인 원소를 찾고.. 반복.
for i in range(len(res_idx)-1, -1, -1):
    if res_idx[i] == cnt:
        cnt -= 1
        q.appendleft(lines[i])
        
print(len(q))
print(*q)
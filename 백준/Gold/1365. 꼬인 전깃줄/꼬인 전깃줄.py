import bisect
from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

arr = list(map(int, input().split()))

res = []
for k in arr:
    a = bisect.bisect_left(res, k)
    if a == len(res):
        res.append(k)
    else:
        res[a] = k

print(str(len(arr) - len(res)))
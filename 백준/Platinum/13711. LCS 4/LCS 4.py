import bisect
from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dicA = {A[i]: i for i in range(len(A))}
dicB = {B[i]: i for i in range(len(B))}

arr = []
for i in range(N):
    arr.append(dicB[A[i]])

res = []
for k in arr:
    a = bisect.bisect_left(res, k)
    if a == len(res):
        res.append(k)
    else:
        res[a] = k

print(str(len(res)))
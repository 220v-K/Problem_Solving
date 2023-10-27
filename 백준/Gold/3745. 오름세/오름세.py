import bisect
from collections import deque

while(True):
    try:
        N = int(input())

        arr = list(map(int, input().split()))

        res = []
        for k in arr:
            a = bisect.bisect_left(res, k)
            if a == len(res):
                res.append(k)
            else:
                res[a] = k

        print(len(res))
    except:
        break
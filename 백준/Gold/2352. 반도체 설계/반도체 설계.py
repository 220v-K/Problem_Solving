import bisect
n = int(input())

lines = list(map(int, input().split()))

# lines의 LIS 길이를 구하면 됨.
res = []
for i in lines:
    a = bisect.bisect_left(res, i)
    if a == len(res):
        res.append(i)
    else:
        res[a] = i
        
print(len(res))
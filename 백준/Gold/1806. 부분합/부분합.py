N, S = map(int, input().split())
nums = list(map(int, input().split()))

'''sums[i] = Sigma[k=0 to i] (nums[k])'''
sums = [nums[0]]
for i in range(1, N):
    sums.append(sums[i-1]+nums[i])

result = N+1
'''index: n ~ m 인 구간합 (S[m] - S[n-1])'''
n = 0
m = 0

while m < N:
    if sums[m] - (0 if n <= 0 else sums[n-1]) >= S:
        if result > m - n + 1:
            result = m - n + 1

        if n >= m:
            m += 1
        else:
            n += 1
    else:
        m += 1

if result == N+1:
    result = 0

print(result)
N, M = map(int, input().split())

nums = list(map(int, input().split()))
dp = [nums[0]]

for i in range(1, N):
    dp.append(dp[i-1]+nums[i])

results = []

for _ in range(M):
    i, j = map(int, input().split())

    if i == 1:
        results.append(dp[j-1])
    else:
        results.append(dp[j-1] - dp[i-2])

for r in results:
    print(r)
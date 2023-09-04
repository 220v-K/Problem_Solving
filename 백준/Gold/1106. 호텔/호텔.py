C, N = map(int, input().split())

inputList = [list(map(int, input().split())) for _ in range(N)]
# dp[i] -> i명을 모았을 때 드는 비용의 최솟값.
dp = [1e9]*(C+101)
dp[0] = 0

for cost, man in inputList:
    for i in range(man, C+100):
        dp[i] = min(dp[i-man]+cost, dp[i])

print(min(dp[C:]))

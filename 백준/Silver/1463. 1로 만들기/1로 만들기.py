N = int(input())
cnt = 0

'''dp[n] = n에서 1을 만들 수 있는 최소의 연산 횟수 (memoization)'''
dp = dict([])

dp[1] = 0
n = 1
for i in range(1, N):
    dp[i+1] = min(dp.get(i+1, N), dp[i]+1)
    dp[i*2] = min(dp.get(i*2, N), dp[i]+1)
    dp[i*3] = min(dp.get(i*3, N), dp[i]+1)

print(dp[N])
T = int(input())

# dp[k]는 정수 k를 1, 2, 3의 합으로 나타내는 방법의 수를 저장.
dp = []
dp.append(0)    # dp[0] = 0
dp.append(1)    # dp[1] = 1
dp.append(2)    # dp[2] = 2
dp.append(4)    # dp[3] = 4

for k in range(4, 12):
    # dp[k-3]+dp[k-2]+dp[k-1] = dp[k]
    dp.append(dp[k-3]+dp[k-2]+dp[k-1])

for _ in range(T):
    print(dp[int(input())])
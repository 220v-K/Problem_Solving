N, M = map(int, input().split())

memory = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0 for _ in range(sum(c)+1)] for _ in range(N+1)]

# dp[i][j] => 1~i번째 앱까지, j의 cost로 확보 가능한 메모리의 최대
for i in range(1, N+1):
    for j in range(0, sum(c)+1):
        if j >= c[i-1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i-1]]+memory[i-1])
        else:
            dp[i][j] = dp[i-1][j]

for i, mem in enumerate(dp[N]):
    if mem >= M:
        print(i)
        break
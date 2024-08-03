k, n = map(int, input().split())
dp = [[-1]*200 for _ in range(200)]

def swim(sec: int, loc: int):
    if dp[sec][loc] != -1:
        return dp[sec][loc]
    
    if loc == 0:
        dp[sec][loc] = 2**sec
        return 2**sec
    if sec == 0:
        return 0

    dp[sec][loc] = swim(sec-1, loc-1) + swim(sec-1, loc+1)
    return dp[sec][loc]

swim(n, k)
print(2**n - dp[n][k])
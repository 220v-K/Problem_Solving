dp = dict()
test = [int(input()) for _ in range(int(input()))]


def fib(n):
    if dp.get(n, -1) != -1:
        return dp[n]
    elif n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        dp[n] = [fib(n-1)[0]+fib(n-2)[0], fib(n-1)[1]+fib(n-2)[1]]
        return dp[n]


for i in test:
    print(*fib(i))

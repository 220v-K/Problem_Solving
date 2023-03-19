n, m = map(int, input().split())

name = [int(input()) for _ in range(n)]

# dp 테이블 초기화, 기저 상태(dp[n+1]) 설정
maxNum = m*m*n
dp = [maxNum] * (n+1)
dp[n] = 0


def note(index: int):
    if dp[index] < maxNum:
        return dp[index]

    remain = m - name[index]

    for i in range(index+1, n+1):
        if remain >= 0:
            if i == n:
                dp[index] = 0
                break
            dp[index] = min(dp[index], remain*remain+note(i))
            remain -= name[i] + 1

    return dp[index]


print(note(0))
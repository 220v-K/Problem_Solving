from collections import deque
str1 = input()
str2 = input()

dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        if str2[i-1] == str1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

result = deque([])
i = len(str2)
j = len(str1)
while dp[i][j] != 0:
    if dp[i][j] == dp[i][j-1]:
        j -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        result.appendleft(str2[i-1])
        i -= 1
        j -= 1

print(len(result))
print(*result, sep="")
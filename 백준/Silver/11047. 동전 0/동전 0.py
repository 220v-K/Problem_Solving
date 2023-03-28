N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

cnt = 0
for coin in coins[::-1]:
    while K >= coin:
        K -= coin
        cnt += 1

    if K == 0:
        print(cnt)
        break
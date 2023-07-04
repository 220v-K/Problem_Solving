N, M, K = map(int, input().split())

v = []
for _ in range(N):
    v.append(list(input()))

res = 0

for i in range(K):
    for j in range(K):
        D = dict()
        n, m = 0, 0
        while n*K + i < N:
            m = 0
            while m*K + j < M:
                if D.get(v[n*K + i][m*K + j]):
                    D[v[n*K + i][m*K + j]] += 1
                else:
                    D[v[n*K + i][m*K + j]] = 1
                m += 1
            n += 1

        A = max(D, key=D.get)

        n, m = 0, 0
        while n*K + i < N:
            m = 0
            while m*K + j < M:
                if v[n*K + i][m*K + j] != A:
                    res += 1
                    v[n*K + i][m*K + j] = A
                m += 1
            n += 1

print(res)
for r in v:
    print(*r, sep="")

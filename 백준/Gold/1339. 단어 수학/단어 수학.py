N = int(input())

A = dict()
words = []

for _ in range(N):
    word = list(input())
    words.append(word)
    word = list(reversed(word))
    for i, w in enumerate(word):
        if A.get(w):
            A[w] += pow(10, i)
        else:
            A[w] = pow(10, i)

A = sorted(A.items(), key=lambda x: x[1], reverse=True)

res = 0
for i, a in enumerate(A):
    res += a[1]*(9-i)

print(res)
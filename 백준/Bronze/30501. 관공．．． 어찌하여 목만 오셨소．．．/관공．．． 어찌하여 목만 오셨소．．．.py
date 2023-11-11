N = int(input())
for _ in range(N):
    a = list(input())
    if "S" in a:
        print(*a, sep="")
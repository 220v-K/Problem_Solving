N = int(input())

times = list(map(int, input().split()))
times.sort()

total = 0
l = len(times)
for i in range(l):
    total += times[i]*(l-i)

print(total)
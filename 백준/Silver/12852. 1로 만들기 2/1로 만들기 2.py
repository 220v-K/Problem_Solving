from collections import deque

n = int(input())
deq = deque()
deq.append([n])
ans = []

while deq:
    a = deq.popleft()
    x = a[0]
    if x == 1:
        ans = a
        break

    if x % 3 == 0:
        deq.append([int(x/3)] + a)

    if x % 2 == 0:
        deq.append([int(x/2)] + a)

    deq.append([x-1] + a)

print(len(ans) - 1)
print(*ans[::-1])
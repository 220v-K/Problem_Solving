N = int(input())
sol = list(map(int, input().split()))

i = 0
j = N-1

result = [1000000000, 1000000000]
while i < j:
    if abs(sol[i]+sol[j]) < abs(sum(result)):
        result = [sol[i], sol[j]]

    if sol[i]+sol[j] > 0:
        j -= 1
    elif sol[i]+sol[j] < 0:
        i += 1
    else:
        break

print(*result)
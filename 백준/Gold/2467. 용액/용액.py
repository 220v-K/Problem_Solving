N = int(input())
sol = list(map(int, input().split()))

i = 0
j = N-1

result = [1000000000, 1000000000]
for i in range(N-1):
    lo = i+1
    hi = N-1

    while lo+1 < hi:
        mid = int((lo+hi)/2)
        if sol[i]+sol[mid] < 0:
            lo = mid
        else:
            hi = mid

    temp = []
    if abs(sol[i]+sol[lo]) < abs(sol[i]+sol[hi]):
        temp = [sol[i], sol[lo]]
    else:
        temp = [sol[i], sol[hi]]

    if abs(sum(temp)) < abs(sum(result)):
        result = temp
    if sum(result) == 0:
        break

print(*result)
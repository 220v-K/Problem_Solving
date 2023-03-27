n = int(input())

factorial = 1
for i in range(1, n+1):
    factorial *= i

cnt = 0
for s in list(str(factorial)[::-1]):
    if s == '0':
        cnt += 1
    else:
        break
print(cnt)
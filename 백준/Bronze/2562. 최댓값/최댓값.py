m = 0
n = 0
for i in range(9):
    a = int(input())
    if m < a:
        m = a
        n = i

print(m)
print(n+1)
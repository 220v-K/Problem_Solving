import sys
read = sys.stdin.readline

N = int(read().strip("\n"))
a = list(map(int, read().strip("\n").split()))

a.sort()
sum = 0
answer = 0

if a[0] > 1:
    answer = 1
else:
    for i in a:
        if sum + 1 < i:
            break
        sum += i

# answer�� ���� ����� �ʾ��� �� (�迭 �� �ִ񰪺��� ���� ��� ���� ���� ����)
# ���� ��� ���� �� + 1�� ���� ��.
answer = sum + 1

print(answer)

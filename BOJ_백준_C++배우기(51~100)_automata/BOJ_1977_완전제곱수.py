M = int(input())
N = int(input())

numList = []
# M, N�� 10000 ������ �ڿ���
for i in range(M, N+1):
    for num in range(1, 101):
        if num*num == i:
            numList.append(i)
            break

# numList is not Empty
if numList:
    sum = 0
    for i in numList:
        sum += i

    print(sum)
    print(numList[0])
# numList is Empty
else:
    print(-1)

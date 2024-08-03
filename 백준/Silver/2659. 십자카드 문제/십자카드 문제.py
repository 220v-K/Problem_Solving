from collections import deque
from itertools import product

clockNums = set()

iters = product(range(1, 10), repeat=4)

# 모든 시계수 찾기
for a in iters:
  a = deque(a)
  num = []
  for _ in range(4):
    temp = ""
    for i in range(4):
      temp += str(a[i])
    num.append(int(temp))
    a.append(a.popleft())

  clockNums.add(min(num))

clockNums = sorted(list(clockNums))

# 입력값의 시계수 index
k = deque(map(int, input().split()))
num = []
for _ in range(4):
  temp = ""
  for i in range(4):
    temp += str(k[i])
  num.append(int(temp))
  k.append(k.popleft())

print(clockNums.index(min(num))+1)

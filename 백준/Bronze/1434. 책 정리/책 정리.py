from collections import deque

N, M = map(int, input().split())

boxes = deque(map(int, input().split()))
books = list(map(int, input().split()))

result = 0
temp = boxes.popleft()

for book in books:  
  while temp < book:
    result += temp
    temp = boxes.popleft()
  
  temp -= book

result += temp
while boxes:
  result += boxes.popleft()
  
print(result)
import heapq

N = int(input())
pq = []
for _ in range(N):
    heapq.heappush(pq, int(input()))

result = 0
while len(pq) > 1:
    k = heapq.heappop(pq) + heapq.heappop(pq)
    result += k
    heapq.heappush(pq, k)

print(result)
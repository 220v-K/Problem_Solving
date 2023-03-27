import heapq

h = []
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

for i in range(N):
    a = nums[i]
    if a == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, a)
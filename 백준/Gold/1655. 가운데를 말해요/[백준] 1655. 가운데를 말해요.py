import heapq

cnt = int(input())
inputList = []

for _ in range(cnt):
    inputList.append(int(input()))

minHeap = []
maxHeap = []
middle = inputList[0]

for num in inputList[1:]:
    print(middle)

    if num > middle:
        heapq.heappush(minHeap, num)
    else:
        heapq.heappush(maxHeap, -num)  # Max-Heap을 사용하기 위해 음수로 삽입

    # minHeap(middle 이상의 그룹)이 maxHeap(middle 이하의 그룹)과 개수가 같거나 1개 많아야 함.
    if not (len(minHeap) == len(maxHeap) or len(minHeap) == len(maxHeap) + 1):
        # minHeap(middle 이상의 그룹)이 2개 더 많아져서 균형이 깨진 경우
        if (len(minHeap) == len(maxHeap) + 2):
            heapq.heappush(maxHeap, -middle)  # Max-Heap을 사용하기 위해 음수로 삽입
            middle = heapq.heappop(minHeap)
        # minHeap보다 maxHeap이 1개 더 많아져서 균형이 깨진 경우
        else:
            heapq.heappush(minHeap, middle)
            middle = -heapq.heappop(maxHeap)

print(middle)

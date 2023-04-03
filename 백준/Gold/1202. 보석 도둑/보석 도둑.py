import sys
import heapq
input = sys.stdin.readline
N, K = map(int, input().split())

jewels = []
'''보석을 weight 오름차순으로 정렬.'''
for _ in range(N):
    jewels.append(tuple(map(int, input().split())))
jewels.sort()

bags = []
for _ in range(K):
    bags.append(int(input()))

'''가방 weight 오름차순 정렬'''
bags.sort()

total_value = 0

temp = []
'''모든 가방에 대해 순회'''
for bag in bags:
    '''남은 보석이 존재하고, 보석이 가방에 들어갈 수 있다면 게속 heap에 push.'''
    while jewels:
        if jewels[0][0] <= bag:
            '''temp heap에 넣을 때는, value가 큰 순의 max heap으로. 가능한 것 중 제일 큰 value를 가진 보석을 택해야 함.'''
            '''이 부분이 Greedy!'''
            heapq.heappush(temp, (-jewels[0][1], jewels[0][0]))
            heapq.heappop(jewels)
        else:
            '''남아있는 보석 중 가장 가벼운 보석도 넣지 못한다면, 그 가방은 넣을 보석이 없음.. ^ㅁ^'''
            break

    '''넣을 보석이 남아 있다면, 제일 value가 큰 보석을 택해 넣음.'''
    '''기본적으로 제일 작은 가방->큰 가방 순으로 순회했기 때문에, **temp heap에 들어 있는 보석은 모두 가방에 들어갈 수 있는 상태!!**'''
    if temp:
        total_value += -heapq.heappop(temp)[0]

print(total_value)
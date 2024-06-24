import heapq

hq = []

while(True):
    m, n = map(int, input().split())
    
    if (m==0 and n==0):
        break
    
    for i in range(m, n+1):
        divisorCnt = 0
        for k in range(1, i+1):
            if k*k > i:   # sqrt(i)까지의 개수 x2 = 총 약수 개수
                break
            
            if k*k == i:    # sqrt(i) == k 라면, 약수 개수 1개 추가.
                divisorCnt += 1
            elif i%k == 0:           # 나머지 경우, 2개 추가.
                divisorCnt += 2
                
        # 최대 heap으로 Y가 큰 순, 이후 X가 큰 순으로 정렬.
        heapq.heappush(hq, (-divisorCnt, -i))
    
    Y, X = heapq.heappop(hq)
    print(-X, -Y)
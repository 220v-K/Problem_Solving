import heapq

N, M = map(int, input().split())
graph = {}
# graph 입력
for _ in range(M):
    a, b, t = map(int, input().split())
    if graph.get(a):
        graph[a].append([b, t])
    else:
        graph[a] = [[b, t]]
        
    if graph.get(b):
        graph[b].append([a, t])
    else:
        graph[b] = [[a, t]]

result = [["-"]*(N+1) for _ in range(N+1)]

# i부터 시작하는 다익스트라
for i in range(1, N+1):
    # 최단 시간 기록 배열
    time = [1e9]*(N+1)
    time[i] = 0
    # 최단 경로 도달 루트 저장 (최단 경로에서 목적지에 도착하기 직전의 노드를 저장)
    route = [0]*(N+1)

    q = []
    heapq.heappush(q, (0, i))

    while q:
        t, n = heapq.heappop(q)
        
        # 새로운 경로에 걸리는 시간이 기존 경로보다 오래 걸리면 pass.
        if time[n] < t:
            continue
        
        for now, cost in graph[n]:
            newCost = t + cost
            if newCost < time[now]:
                time[now] = newCost
                route[now] = n
                heapq.heappush(q, (newCost, now))
            
    # i -> j 최단경로의 처음 거치는 노드 추적
    for j in range(1, N+1):
        if i==j:
            continue
        
        now = j
        while result[i][j] == "-":
            # 직전이 시작 노드라면
            if route[now] == i:
                result[i][j] = now
            else:
                now = route[now]
    
for i in range(1, N+1):
    print(*result[i][1:])
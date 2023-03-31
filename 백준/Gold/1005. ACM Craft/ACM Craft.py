from collections import deque
T = int(input())
result = []

for _ in range(T):
    N, K = map(int, input().split())
    times = list(map(int, input().split()))

    '''그래프 저장'''
    graph_in_cnt = dict()
    graph_in = dict()
    graph_out = dict()
    for _ in range(K):
        a, b = map(int, input().split())
        '''위상 정렬(Topological Sort)에서는 나가는 간선의 수(진출 차수)와 들어오는 간선의 수(진입 차수)가 모두 필요.'''
        if graph_out.get(a):
            graph_out[a].append(b)
        else:
            graph_out[a] = [b]

        if graph_in.get(b):
            graph_in[b].append(a)
        else:
            graph_in[b] = [a]

        if graph_in_cnt.get(b):
            graph_in_cnt[b] += 1
        else:
            graph_in_cnt[b] = 1

    '''지어야 하는 건물의 번호 W 저장'''
    W = int(input())

    '''진입 차수가 0인 vertex를 queue에 삽입'''
    queue = deque([])
    for i in range(1, N+1):
        if not graph_in_cnt.get(i) or graph_in[i] == 0:
            queue.append(i)

    queue_copy = queue
    total_time = 0

    dp = dict()

    '''Bottom-Up 형식의 DP'''
    while queue:
        '''queue에서 vertex pop'''
        a = queue.popleft()
        '''queue에서 pop하여 연결된 vertex들의 진입 차수 1씩 감소, 진입 차수가 0이 되었다면 queue에 추가'''
        for t in graph_out.get(a, []):
            graph_in_cnt[t] -= 1
            if graph_in_cnt[t] == 0:
                queue_copy.append(t)

        '''a를 짓는 데 걸리는 최소의 시간.'''
        '''만약 graph_in[a] = [b, c]라면, dp[a] = max(dp[b], dp[c]) + times[a-1]가 될 것이다.'''
        if not graph_in.get(a):
            dp[a] = times[a-1]
        else:
            max_prepare = 0
            for building in graph_in[a]:
                if max_prepare < dp[building]:
                    max_prepare = dp[building]

            dp[a] = max_prepare + times[a-1]

        if a == W:
            result.append(dp[a])
            break

for i in result:
    print(i)
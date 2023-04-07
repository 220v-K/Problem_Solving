from collections import deque
N = int(input())

times = []
graph_in_cnt = dict([])
graph_in = dict([])
graph_out = dict([])

'''input 처리'''
for i in range(N):
    a = list(map(int, input().split()))
    times.append(a[0])
    graph_in_cnt[i+1] = a[1]
    graph_in[i+1] = a[2:]
    for o in a[2:]:
        if graph_out.get(o):
            graph_out[o].append(i+1)
        else:
            graph_out[o] = [i+1]

queue = deque([])
'''진입 차수가 0인 작업 queue에 append.'''
for i, n in enumerate(graph_in_cnt):
    if graph_in_cnt[n] == 0:
        queue.append(i+1)

dp = dict([])
while queue:
    a = queue.popleft()

    for k in graph_out.get(a, []):
        graph_in_cnt[k] -= 1
        if graph_in_cnt[k] == 0:
            queue.append(k)

    '''dp[a] = a를 짓는 데 걸리는 최소 시간'''
    '''진입 차수가 0이라면, 본인의 건설 시간'''
    '''진입 차수가 0이 아니라면, 앞서 지어야 하는 것들의 최소 건설 시간 중 최댓값 + 본인의 건설 시간'''
    '''ex) graph_in[a] = [b,c]라면, dp[a] = max(dp[b], dp[c]) + times[a-1]'''
    max_time = 0
    for k in graph_in.get(a, []):
        if max_time < dp[k]:
            max_time = dp[k]

    dp[a] = max_time + times[a-1]

print(max(dp.values()))
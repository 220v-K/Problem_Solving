from collections import deque
N, M, V = map(int, input().split())

graph = dict()

# 그래프 저장 (간선 입력)
for _ in range(M):
    a, b = map(int, input().split())

    if graph.get(a, -1) == -1:
        graph[a] = [b]
    else:
        graph[a].append(b)

    if graph.get(b, -1) == -1:
        graph[b] = [a]
    else:
        graph[b].append(a)

stack = deque([V])
visited = []

# DFS
while stack:
    v = stack.pop()

    if v in visited:
        continue
    else:
        if graph.get(v, -1) == -1:
            visited.append(v)
            continue
        stack.extend(sorted(graph[v], key=lambda x: -x))
        visited.append(v)

print(*visited)

# BFS

queue = deque([V])
visited = []

while queue:
    v = queue.popleft()

    if v in visited:
        continue
    else:
        if graph.get(v, -1) == -1:
            visited.append(v)
            continue
        queue.extend(sorted(graph[v], key=lambda x: x))
        visited.append(v)

print(*visited)
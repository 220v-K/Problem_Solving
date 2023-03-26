from collections import deque

N, M = map(int, input().split())

'''그래프 저장(간선 입력), 초기값은 최댓값인 N로 설정. 정점이 N개이므로 최대로 나올 수 있는 가중치는 N-1임.'''
graph = [[N]*N for _ in range(N)]

'''자기 자신으로의 weight=0으로'''
for i in range(N):
    graph[i][i] = 0

'''간선 입력받아 가중치 1로 설정'''
for _ in range(M):
    a, b = map(int, input().split())

    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

'''Floyd-Warshall'''
for i in range(N):
    for r, row in enumerate(graph):
        for c, col in enumerate(row):
            if r == c or r == i or c == i:
                continue
            graph[r][c] = min(graph[r][c], graph[r][i]+graph[i][c])


graph = list(map(sum, graph))
'''최소값을 가진 index 중 가장 작은 것'''
index = 0
minimum = N*N
for i in range(N):
    if graph[i] < minimum:
        index = i
        minimum = graph[i]

print(index+1)
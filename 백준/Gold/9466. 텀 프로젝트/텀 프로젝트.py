import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())
 
def dfs(x):
    global cnt
    visited[x] = True
    i = graph[x]
    if not visited[i]:
        dfs(i)
    else:
        if i not in team:
            nxt = i
            while nxt != x:
                cnt += 1
                nxt = graph[nxt]
            cnt += 1
 
    team.add(x)
 
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int,input().split()))
    visited = [False] * (n+1)
    team = set()
 
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
 
    print(n - cnt)
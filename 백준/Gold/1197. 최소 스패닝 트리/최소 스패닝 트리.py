V, E = map(int, input().split())
edges = []
'''간선 정보 입력 (V1, V2, Edge's cost)'''
for _ in range(E):
    edges.append(list(map(int, input().split())))

'''Union-Find 구현'''
root = dict()
for i in range(1, V+1):
    root[i] = i


def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]


def union(x, y):
    x = find(x)
    y = find(y)

    root[y] = x


'''Kruskal 이용'''
'''Edge cost 오름차순으로 정렬'''
edges = sorted(edges, key=lambda x: x[2])

total_cost = 0

for edge in edges:
    '''사이클이 만들어지는 edge라면 pass.'''
    if find(edge[0]) == find(edge[1]):
        continue
    else:
        total_cost += edge[2]
        union(edge[0], edge[1])

print(total_cost)
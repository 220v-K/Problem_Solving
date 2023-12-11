N = int(input())

# Union-Find 구현
root = {i: i for i in range(N)}

def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    rx = find(x)
    ry = find(y)
    
    if rx == ry:
        return
    
    if rx > ry:
        root[ry] = rx
    else:
        root[rx] = ry
        
########

coorX = []
coorY = []
coorZ = []
# 입력 및 x, y, z 좌표별 좌표값과 index append / 좌표값에 따라 오름차순 정렬
for i in range(N):
    x, y, z = map(int, input().split())
    coorX.append((x, i))
    coorY.append((y, i))
    coorZ.append((z, i))
coorX = sorted(coorX, key=lambda x: x[0])
coorY = sorted(coorY, key=lambda x: x[0])
coorZ = sorted(coorZ, key=lambda x: x[0])

# Kruskal - 가중치, edge의 양 끝 vertex 저장.
edges = []
for i in range(N-1):
    edges.append( (abs(coorX[i+1][0]-coorX[i][0]), coorX[i][1], coorX[i+1][1]) )
    edges.append( (abs(coorY[i+1][0]-coorY[i][0]), coorY[i][1], coorY[i+1][1]) ) 
    edges.append( (abs(coorZ[i+1][0]-coorZ[i][0]), coorZ[i][1], coorZ[i+1][1]) ) 

# Kruskal - 가중치 순 정렬    
edges.sort()

# Kruskal - MST 생성 및 cost 계산
result = 0
for edge in edges:
	cost, a, b = edge
	if find(a) != find(b):
		union(a, b)
		result += cost
  
print(result)
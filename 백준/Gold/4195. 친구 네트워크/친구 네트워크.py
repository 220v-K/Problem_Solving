T = int(input())

root = {}
cnt = {}

def find(x):
    if root[x] == x:
        return x
    # 경로 압축
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    if x > y:
        root[x] = y
        # y를 root로 설정했으니, y의 네트워크 수에 x의 네트워크 수를 더해서 저장.
        cnt[y] += cnt[x]
    else :
        root[y] = x
        # x를 root로 설정했으니, x의 네트워크 수에 y의 네트워크 수를 더해서 저장.
        cnt[x] += cnt[y]

for _ in range(T):
    F = int(input())
    root = {}   # Union-Find root
    cnt = {}    # 친구 네트워크에 있는 사람 수
    
    for _ in range(F):
        a, b = input().split()
        if a not in root:
            root[a] = a
            cnt[a] = 1
        if b not in root:
            root[b] = b
            cnt[b] = 1
        union(a, b)
        print(cnt[find(a)])
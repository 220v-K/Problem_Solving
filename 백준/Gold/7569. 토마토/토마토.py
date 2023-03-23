import copy
from collections import deque

width, height, depth = map(int, input().split())
box = []
for _ in range(depth):
    box.append([list(map(int, input().split())) for _ in range(height)])


# 시작 상황에서 모든 익은 토마토의 좌표를 queue에 push
deq = deque([])
for z, d in enumerate(box):
    for y, h in enumerate(d):
        for x, w in enumerate(h):
            if w == 1:
                # z, y, x 좌표순
                deq.append([z, y, x])

# 토마토의 좌표는 box[z][y][x]입니다.
dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]

cnt = 0


def isFin(box):
    for a in box:
        for b in a:
            for c in b:
                if c == 0:
                    return False
    return True


while deq:
    # 토마토가 모두 익었으면
    if isFin(box):
        print(cnt)
        break
    cnt += 1

    # 이번에 전후좌우상하를 익힐 익은 토마토들 - deq_에 저장
    deq_ = copy.deepcopy(deq)
    # 오늘 익은 토마토들 - deq를 초기화시켜 저장
    deq = deque([])

    # 익은 토마토를 기준으로 전후좌우상하 6방향의 토마토를 익힘
    while deq_:
        z, y, x = deq_.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 이미 visit한 토마토는 box[nz][ny][nx] == 1 이기 때문에 pass. deq에도 push되지 않음.
            if 0 <= nx < width and 0 <= ny < height and 0 <= nz < depth and box[nz][ny][nx] == 0:
                box[nz][ny][nx] = 1
                deq.append([nz, ny, nx])


# 토마토가 모두 익지 않았으면
if not isFin(box):
    print(-1)

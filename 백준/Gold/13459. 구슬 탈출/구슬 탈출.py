from collections import deque
N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

redr, redc, bluer, bluec = 0, 0, 0, 0
# Red, Blue 구슬 위치 찾기
for r in range(N):
    for c in range(M):
        if graph[r][c] == "R":
            redr, redc = r, c
        if graph[r][c] == "B":
            bluer, bluec = r, c

visited = []
deq = deque([(redr, redc, bluer, bluec, 0)])
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
success = []

def move(nr, nc, dr, dc):
    moveCnt = 0
    # 벽 또는 구멍을 만날 때까지 이동
    while graph[nr+dr][nc+dc] != "#" and graph[nr][nc] != "O":
        nr, nc = nr+dr, nc+dc
        moveCnt += 1
    
    return nr, nc, moveCnt

while deq:
    redr, redc, bluer, bluec, time = deq.popleft()
    time += 1
    
    if time > 10: continue
    
    for i in range(4):
        redlr, redlc, redMove = move(redr, redc, dr[i], dc[i])
        bluelr, bluelc, blueMove = move(bluer, bluec, dr[i], dc[i])
        
        # 파란 구슬이 구멍에 들어갔다면 실패
        if graph[bluelr][bluelc] == "O":
            continue
        # 파란 구슬이 구멍에 들어가지 않고, 빨간 구슬이 구멍에 들어갔다면 성공
        if graph[redlr][redlc] == "O":
            success.append(time)
            
        # 이동 후 겹쳐있다면, 더 많이 이동한 구슬을 한 칸 당김
        if redlr == bluelr and redlc == bluelc:
            if redMove > blueMove:
                redlr, redlc = redlr-dr[i], redlc-dc[i]
            else:
                bluelr, bluelc = bluelr-dr[i], bluelc-dc[i]
        
        # visited 확인 및 방문 체크
        if (redlr, redlc, bluelr, bluelc) in visited:
            continue
        visited.append((redlr, redlc, bluelr, bluelc))
        
        deq.append((redlr, redlc, bluelr, bluelc, time))

if success: print(1)
else: print(0)
from collections import deque
test_case_cnt = int(input())
# 결과값 저장
worms = []

# 배추의 좌표를 임시 저장하는 변수
cab = []

# 배추가 싹 사라졌나요??


def isCabClear():
    for y, row in enumerate(field):
        for x, c in enumerate(row):
            if c == 1:
                cab.append([x, y])
                return False
    return True


for _ in range(test_case_cnt):
    worm_cnt = 0
    row, col, cab_num = map(int, input().split())

    # 배추밭 생성 뿅! 좌표는 x=3, y=4라면 field[4][3]처럼 접근해야 함! (column이 바깥쪽 차원)
    field = [[0]*row for _ in range(col)]

    # 배추를 심자 쏙쏙
    for _ in range(cab_num):
        r, c = map(int, input().split())
        field[c][r] = 1

    # 지렁이 마리수
    worm_cnt = 0

    # 먹을 배추~ (BFS에서의 Queue)
    deq = deque([])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while not isCabClear():
        deq.append(cab.pop())
        while deq:
            x, y = deq.popleft()
            field[y][x] = 0
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                # 밭의 경계(M, N)을 벗어나지 않고, 배추가 있다면
                if 0 <= nx < row and 0 <= ny < col and field[ny][nx] == 1:
                    # 배추 먹고 큐에 추가
                    field[ny][nx] = 0
                    deq.append([nx, ny])

        worm_cnt += 1
    worms.append(worm_cnt)

for cnt in worms:
    print(cnt)

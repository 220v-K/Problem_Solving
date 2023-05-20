N = int(input())
q = []
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

q.append([0, 0])

while q:
    row, col = q.pop()

    a = board[row][col]

    if a == -1:
        print("HaruHaru")
        exit()

    if a == 0:
        continue

    if row+a < N:
        q.append([row+a, col])
    if col+a < N:
        q.append([row, col+a])

print("Hing")
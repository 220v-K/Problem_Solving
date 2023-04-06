board = [list(map(int, input())) for _ in range(9)]
coors = []
'''0이 들어간 좌표 저장'''
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            coors.append((i, j))


'''rowCheck[n][m-1] = n번 row에 m이 포함되었는지'''
rowCheck = [[False] * 9 for _ in range(9)]
'''colCheck[n][m-1] = n번 column에 m이 포함되었는지'''
colCheck = [[False] * 9 for _ in range(9)]
'''boxCheck[n][m-1] = n번 box에 m이 포함되었는지'''
boxCheck = [[False] * 9 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            boxCheck[(i//3)*3 + j//3][board[i][j]-1] = True
            rowCheck[i][board[i][j]-1] = True
            colCheck[j][board[i][j]-1] = True


def backT(n):
    '''coors(0의 좌표들) 의 개수만큼 depth가 깊어졌다면, 모든 0에 숫자를 채워넣은 상태이므로, 종료.'''
    if n == len(coors):
        for b in board:
            print(*b, sep="")
        exit()

    '''i, j = row, column'''
    i, j = coors[n]
    for k in range(1, 10):
        if rowCheck[i][k-1]:
            continue
        if colCheck[j][k-1]:
            continue
        if boxCheck[(i//3)*3 + j//3][k-1]:
            continue

        '''row, col, box check 후 숫자 삽입'''
        board[i][j] = k
        boxCheck[(i//3)*3 + j//3][k-1] = True
        rowCheck[i][k-1] = True
        colCheck[j][k-1] = True

        backT(n+1)

        '''만약 더 깊은 depth에서 return이 일어났다면, backTracking을 위해 원상복구.'''
        board[i][j] = 0
        boxCheck[(i//3)*3 + j//3][k-1] = False
        rowCheck[i][k-1] = False
        colCheck[j][k-1] = False


backT(0)
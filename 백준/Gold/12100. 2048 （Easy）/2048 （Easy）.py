import sys
import copy
sys.setrecursionlimit(2**11)
N = int(input())

Board = [list(map(int, input().split())) for _ in range(N)]

result_max = []


def left(board):
    for row in board:
        # 왼쪽으로 당기기
        tempIndex = 0
        for index in range(N):
            if row[index] != 0:
                # 0과 오른쪽의 숫자를 swap하여 왼쪽으로 당김
                row[index], row[tempIndex] = row[tempIndex], row[index]
                tempIndex += 1

        # 왼쪽으로 밀면서 같은 숫자 합치기
        temp = 0
        index = 0
        while index < N:
            if row[index] == 0:
                # 왼쪽으로 이미 밀었으므로, 0을 만나면 종료
                break
            else:
                # 앞의 숫자와 같다면
                if temp == row[index]:
                    row[index-1] *= 2
                    # 앞의 숫자를 2배로 하고, 뒤의 숫자들을 하나씩 당김
                    j = index
                    while j < N-1:
                        row[j] = row[j+1]
                        j += 1
                    row[-1] = 0
                    temp = 0
                    # 합쳐져서 한 칸 당겼다면 다시 그 index부터 검사
                    index -= 1
                else:
                    temp = row[index]

            index += 1
    return board


def right(board):
    for row in board:
        # 오른쪽으로 당기기
        tempIndex = N-1
        for index in range(N-1, -1, -1):
            if row[index] != 0:
                # 0과 왼쪽의 숫자를 swap하여 오른쪽으로 당김
                row[index], row[tempIndex] = row[tempIndex], row[index]
                tempIndex -= 1

        # 오른쪽으로 밀면서 같은 숫자 합치기
        temp = 0
        index = N-1
        while index >= 0:
            if row[index] == 0:
                # 오른쪽으로 이미 밀었으므로, 0을 만나면 종료
                break
            else:
                # 뒤의 숫자와 같다면
                if temp == row[index]:
                    row[index+1] *= 2
                    # 뒤의 숫자를 2배로 하고, 뒤의 숫자들을 하나씩 당김
                    j = index
                    while j > 0:
                        row[j] = row[j-1]
                        j -= 1
                    row[0] = 0
                    temp = 0
                    # 합쳐져서 한 칸 당겼다면 다시 그 index부터 검사
                    index += 1
                else:
                    temp = row[index]

            index -= 1
    return board


def up(board):
    for col in range(N):
        # column = board[0 ~ N-1][col]
        # 위로 당기기
        tempIndex = 0
        for index in range(N):
            if board[index][col] != 0:
                # 0과 아래의 숫자를 swap해 위로 당김
                board[index][col], board[tempIndex][col] = board[tempIndex][col], board[index][col]
                tempIndex += 1

        # 위로 밀면서 같은 숫자 합치기
        temp = 0
        index = 0
        while index < N:
            if board[index][col] == 0:
                # 위로 이미 밀었으므로, 0을 만나면 종료
                break
            else:
                # 위의 숫자와 같다면
                if temp == board[index][col]:
                    # 위의 숫자를 2배로 하고, 아래부터 한칸씩 당김
                    board[index-1][col] *= 2
                    j = index
                    while j < N-1:
                        board[j][col] = board[j+1][col]
                        j += 1
                    board[-1][col] = 0
                    temp = 0
                    index -= 1
                else:
                    temp = board[index][col]

            index += 1
    return board


def down(board):
    for col in range(N):
        # column = board[0 ~ N-1][col]
        # 아래로 당기기
        tempIndex = N-1
        for index in range(N-1, -1, -1):
            if board[index][col] != 0:
                # 0과 위의 숫자를 swap해 아래로 당김
                board[index][col], board[tempIndex][col] = board[tempIndex][col], board[index][col]
                tempIndex -= 1

        # 아래로 밀면서 같은 숫자 합치기
        temp = 0
        index = N-1
        while index >= 0:
            if board[index][col] == 0:
                # 아래로 이미 밀었으므로, 0을 만나면 종료
                break
            else:
                # 아래의 숫자와 같다면
                if temp == board[index][col]:
                    # 아래의 숫자를 2배로 하고, 아래부터 한칸씩 당김
                    board[index+1][col] *= 2
                    j = index
                    while j > 0:
                        board[j][col] = board[j-1][col]
                        j -= 1
                    board[0][col] = 0
                    temp = 0
                    index += 1
                else:
                    temp = board[index][col]

            index -= 1
    return board


def dfs(board, depth: int):
    if depth == 5:
        result_max.append(max(map(max, board)))
        return
    # left
    dfs(left(copy.deepcopy(board)), depth+1)
    # right
    dfs(right(copy.deepcopy(board)), depth+1)
    # up
    dfs(up(copy.deepcopy(board)), depth+1)
    # down
    dfs(down(copy.deepcopy(board)), depth+1)


dfs(copy.deepcopy(Board), 0)

print(max(result_max))
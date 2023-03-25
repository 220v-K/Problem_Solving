Num, col, row = map(int, input().split())


def A(N, r, c):
    middle = pow(2, N-1)
    if r < middle and c < middle:
        return 0
    elif r >= middle and c < middle:
        return 1
    elif r < middle and c >= middle:
        return 2
    elif r >= middle and c >= middle:
        return 3


def sol(N, r, c):
    if N == 1:
        return A(N, r, c)

    middle = pow(2, N-1)
    area = A(N, r, c)
    if r >= middle:
        r -= middle
    if c >= middle:
        c -= middle

    return area*(int(pow(pow(2, N), 2) / 4)) + sol(N-1, r, c)


print(sol(Num, row, col))
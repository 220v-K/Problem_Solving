from collections import deque
import sys
input = sys.stdin.readline


def sol():

    N, K = map(int, input().split())

    deq = deque([N])
    visit = dict()
    visit[N] = 0
    while deq:
        a = deq.popleft()
        if a == K:
            print(visit[a])
            return

        for i in [a*2, a+1, a-1]:
            if 0 <= i <= 100000 and visit.get(i, -1) == -1:
                deq.append(i)
                visit[i] = visit[a]+1

sol()
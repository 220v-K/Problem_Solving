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

        if 0 <= a*2 <= 100000 and visit.get(a*2, -1) == -1:
            deq.append(a*2)
            visit[a*2] = visit[a]+1
        if 0 <= a+1 <= 100000 and visit.get(a+1, -1) == -1:
            deq.append(a+1)
            visit[a+1] = visit[a]+1
        if 0 <= a-1 <= 100000 and visit.get(a-1, -1) == -1:
            deq.append(a-1)
            visit[a-1] = visit[a]+1


sol()

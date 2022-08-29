from collections import deque


def solution(n, path, order):
    pre = {i[0]: i[1] for i in order}
    follow = {i[1]: i[0] for i in order}

    visit = set([0])
    rooms = deque([0])
    rooms_wait = set()  # �������Ƕ����� �� ���� �� �־�α�
    graph = {i: [] for i in range(n)}

    for p in path:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])

    while rooms:
        room = rooms.popleft()

        # ���� ���� X
        if room in follow:
            rooms_wait.add(room)
        # �ɸ��� ������ ���� ��
        else:
            visit.add(room)
            # �������� �ذ�
            if room in pre:
                i = pre[room]
                del pre[room]
                if i in rooms_wait:
                    rooms.append(i)
                    rooms_wait.remove(i)
                del follow[i]

            for n in graph[room]:
                if n not in visit and n not in rooms_wait and n != room:
                    rooms.append(n)

    if rooms_wait:
        return (False)
    else:
        return (True)

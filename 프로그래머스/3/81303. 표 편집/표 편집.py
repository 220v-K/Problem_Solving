def solution(n, k, cmd):
    stack = []

    # {i: [active, prevPtr, nextPtr]}
    table = {i: [True, i-1, i+1] for i in range(n)}

    ptr = k

    for c in cmd:
        if c[0] == "U":
            x = int(c.split()[1])
            for _ in range(x):
                ptr = table[ptr][1]

        elif c[0] == "D":
            x = int(c.split()[1])
            for _ in range(x):
                ptr = table[ptr][2]

        elif c[0] == "C":
            stack.append(ptr)   # 스택에 저장
            table[ptr][0] = False

            # if ptr.prev != -1
            if table[ptr][1] > -1:
                # ptr.prev.next = ptr.next
                table[table[ptr][1]][2] = table[ptr][2]
            # if ptr.next != n
            if table[ptr][2] < n:
                # ptr.next.prev = ptr.prev
                table[table[ptr][2]][1] = table[ptr][1]

            # if ptr.next == n
            if table[ptr][2] == n:
                # ptr = ptr.prev
                ptr = table[ptr][1]
            else:
                # ptr = ptr.next
                ptr = table[ptr][2]

        else:   # c[0] == "Z"
            x = stack.pop()
            table[x][0] = True
            # 어짜피 먼저 삭제된 것 부터 복구되므로,
            # 복구할 node의 prev와 next는 항상 지워지지 않은 상태임이 보장됨.
            # 또한, 복구할 node와, 그 node의 prev와 next 사이에 어떤 node도 존재하지 않음이 보장되므로,
            # 복구할 node의 prev와 next를 변경하지 않아도 됨.

            # 복구할 node의 prev.next와 next.prev 복구
            # if x.prev != -1
            if table[x][1] > -1:
                # x.prev.next = x
                table[table[x][1]][2] = x
            # if x.next != n
            if table[x][2] < n:
                # x.next.prev = x
                table[table[x][2]][1] = x

    answer = ""
    for i in range(n):
        if table[i][0]:
            answer += "O"
        else:
            answer += "X"
            
    return answer
import sys
input = sys.stdin.readline
M = int(input())

a = set()
for _ in range(M):
    c = list(input().split())
    if len(c) == 2:
        command, num = c
        num = int(num)
    else:
        command = c[0]
        if command == 'all':
            a = set([i for i in range(1, 21)])
        elif command == 'empty':
            a = set()

    if command == 'add':
        a.add(num)
    elif command == 'remove':
        a.discard(num)
    elif command == 'check':
        if num in a:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if num in a:
            a.discard(num)
        else:
            a.add(num)

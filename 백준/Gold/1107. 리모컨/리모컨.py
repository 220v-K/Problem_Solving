import sys

input = sys.stdin.readline
current = 100
goal = int(input())
break_cnt = int(input())
button = [i for i in range(10)]
breakButton = []
if break_cnt != 0:
    breakButton = list(map(int, input().split()))
button = list(set(button) - set(breakButton))


# 이동하려는 채널이 1~500,000이기 때문에 Brute Force로 접근해도 할만 함.
# 6자리 내에서 모든 만들 수 있는 수의 경우를 만들고, goal과의 수 차이를 측정.

channels = dict([])
# 1~6자리수의 가능한 모든 조합을 dictionary에 저장
for a in button:
    channels[a] = 0
    for b in button:
        channels[int(str(a)+str(b))] = 0
        for c in button:
            channels[int(str(a)+str(b)+str(c))] = 0
            for d in button:
                channels[int(str(a)+str(b)+str(c)+str(d))] = 0
                for e in button:
                    channels[int(str(a)+str(b)+str(c)+str(d)+str(e))] = 0
                    for f in button:
                        channels[int(str(a)+str(b)+str(c) +
                                     str(d)+str(e)+str(f))] = 0

# 모든 채널에 대해
for ch in channels:
    # 100에서 움직일 때와 버튼을 누르고 움직일 때, 둘 중 최솟값을 채택
    channels[ch] = min(abs(goal - 100), len(str(ch)) + abs(goal - ch))

if channels:
    print(channels[min(channels, key=channels.get)])
else:
    print(abs(goal - 100))

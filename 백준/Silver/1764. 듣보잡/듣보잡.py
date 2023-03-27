N, M = map(int, input().split())

dut = dict()
for _ in range(N):
    dut[input()] = 0

bo = dict()
for _ in range(M):
    bo[input()] = 0

dutbo = []
for name in dut:
    if bo.get(name, -1) == 0:
        dutbo.append(name)

print(len(dutbo))
for name in list(sorted(dutbo)):
    print(name)
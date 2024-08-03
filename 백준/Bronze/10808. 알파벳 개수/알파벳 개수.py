S = list(input())

d = {i: 0 for i in range(97, 123)}

for s in S:
  d[ord(s)] += 1

print(*d.values())
N = int(input())
s = list(map(int, input().split()))

satis = 0   # s_i의 총합을 저장
result = 0  # 현재 만족도를 저장

for i in range(N):
    if result < s[i] - satis:    # 현재 만족도보다 새치기의 이득이 높다면
        result = s[i] - satis
    
    satis += s[i]

print(result)
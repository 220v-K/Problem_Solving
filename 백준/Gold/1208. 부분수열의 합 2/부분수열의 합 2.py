N, S = map(int, input().split())
nums = list(map(int, input().split()))

nums1 = nums[:int(N/2)]
nums2 = nums[int(N/2):]

sums1 = [0]
for i in nums1:
    temp = []
    for k in sums1:
        temp.append(k+i)
    sums1.extend(temp)

sums2 = [0]
for i in nums2:
    temp = []
    for k in sums2:
        temp.append(k+i)
    sums2.extend(temp)

sums1 = sorted(sums1)
sums2 = sorted(sums2, key=lambda x: -x)

index1 = 0
index2 = 0

result = 0
while index1 < len(sums1) and index2 < len(sums2):
    tempSum = sums1[index1]+sums2[index2]
    if tempSum == S:
        a = 1
        b = 1
        index1 += 1
        index2 += 1
        while index1 < len(sums1) and sums1[index1] == sums1[index1-1]:
            index1 += 1
            a += 1
        while index2 < len(sums2) and sums2[index2] == sums2[index2-1]:
            index2 += 1
            b += 1
        result += a*b

    elif tempSum > S:
        index2 += 1
    else:
        index1 += 1

if S == 0:
    result -= 1

print(result)
check = [False]*1000000
check[0] = True
nums = [0]

N = int(input())
for i in range(1, 100001):
    a = nums[i-1]-i
    if a < 0:
        a = nums[i-1]+i
    elif check[a]:
        a = nums[i-1]+i
    
    check[a] = True
    nums.append(a)

print(nums[N])
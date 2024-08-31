N = int(input())

left_bottom = [10, 10]
right_top = [-10, -10]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    
    if left_bottom[0] > a:
        left_bottom[0] = a
    if left_bottom[1] > b:
        left_bottom[1] = b
    if right_top[0] < c:
        right_top[0] = c
    if right_top[1] < d:
        right_top[1] = d
        
    width = right_top[0]-left_bottom[0]
    height = right_top[1]-left_bottom[1]
    outline = (width+height)*2
    print(outline)
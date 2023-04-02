N = int(input())

dots = []
for _ in range(N):
    dots.append(list(map(float, input().split())))

area = 0

'''triangle: 1st dot, and ith, (i+1)th dot.'''
for i in range(1, len(dots)-1):
    a = dots[0]
    b = dots[i]
    c = dots[i+1]

    '''vector 1 : (x2-x1, y2-y1)'''
    vec1 = [b[0]-a[0], b[1]-a[1]]
    '''vector 2 : (x3-x2, y3-y1)'''
    vec2 = [c[0]-a[0], c[1]-a[1]]

    '''add triangle's area to total area'''
    area += (vec1[0]*vec2[1] - vec1[1]*vec2[0])/2

print(abs(area))

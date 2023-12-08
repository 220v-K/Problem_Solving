x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def ccw(a1, b1, a2, b2, a3, b3):
    s = (a1*b2 + a2*b3 + a3*b1) - (a2*b1 + a3*b2 + a1*b3)
    
    if s > 0: return 1
    elif s == 0: return 0
    else: return -1
    
print(ccw(x1, y1, x2, y2, x3, y3))
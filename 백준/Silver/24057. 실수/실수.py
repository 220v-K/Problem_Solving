def lcm(a, b):
  return (a * b) / gcd(a, b)

def gcd(a, b):
  if a < 0:
    a = -a
  if b < 0:
    b = -b

  while b != 0:
    r = a % b
    a = b
    b = r

  return a

a1, b1, c1, d1 = map(int, input().split())
a2, b2, c2, d2 = map(int, input().split())

## +, - 계산
# 통분
e = lcm(a1, a2)
a3 = e
b3 = b1*(e/a1)+b2*(e/a2)
c3 = c1*(e/a1)+c2*(e/a2)

a4 = e
b4 = b1*(e/a1)-b2*(e/a2)
c4 = c1*(e/a1)-c2*(e/a2)

# 약분
k = gcd(gcd(a3, b3), gcd(a3, c3))
if k > 1:
  a3 /= k
  b3 /= k
  c3 /= k
k = gcd(gcd(a4, b4), gcd(a4, c4))
if k > 1:
  a4 /= k
  b4 /= k
  c4 /= k

plus = (a3, b3, c3, 0 if c3==0 else d1)
minus = (a4, b4, c4, 0 if c4==0 else d1)

## * 계산
a5 = a1*a2
child1 = b1*b2 + c1*c2*d1 #실수부
child2 = b1*c2 + b2*c1  #허수부

# 약분
if child2 == 0:
  k = gcd(a5, child1)
  product = (a5/k, child1/k, 0, 0)
else:
  k = gcd(gcd(a5, child1), gcd(a5, child2))
  product = (a5/k, child1/k, child2/k, d1)

## / 계산
# 분모의 유리화
mother = a1*(b2**2 - d1*(c2**2))
child1 = a2*(b1*b2 + c1*(-c2)*d1) # 실수부
child2 = a2*(b1*(-c2) + b2*c1) # 허수부

# 약분
if child2 == 0:
  k = gcd(mother, child1)
  division = (mother/k, child1/k, 0, 0)
else:
  k = gcd(gcd(mother, child1), gcd(mother, child2))
  division = (mother/k, child1/k, child2/k, d1)

if division[0] < 0:
  division = (-division[0], -division[1], -division[2], division[3])

print(*map(int, plus))
print(*map(int, minus))
print(*map(int, product))
print(*map(int, division))
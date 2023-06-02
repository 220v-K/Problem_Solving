T = int(input())

result = []

for _ in range(T):
    N = int(input())
    lumber = [*map(int, input().split())]

    lumber = sorted(lumber)
    difficulty = 0

    for i in range(2, len(lumber), 2):
        if difficulty < lumber[i] - lumber[i-2]:
            difficulty = lumber[i] - lumber[i-2]

    if difficulty < lumber[len(lumber)-2] - lumber[len(lumber)-1]:
        difficulty = lumber[len(lumber)-2] - lumber[len(lumber)-1]

    for i in range(1, len(lumber), 2):
        if difficulty < lumber[i] - lumber[i-2]:
            difficulty = lumber[i] - lumber[i-2]

    if difficulty < lumber[1] - lumber[0]:
        difficulty = lumber[1] - lumber[0]

    result.append(difficulty)

for k in result:
    print(k)
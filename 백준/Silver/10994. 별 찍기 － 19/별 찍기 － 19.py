n = int(input())
size = 4 * n - 3

table = [[' ' for _ in range(size)] for _ in range(size)]

for i in range(n):
    start = 2 * i
    end = size - 2 * i - 1
    for j in range(start, end + 1):
        table[start][j] = '*'
        table[end][j] = '*'
        table[j][start] = '*'
        table[j][end] = '*'
        
for row in table:
    print(''.join(row))
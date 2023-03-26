s = input()

buffer = '0'
nums = []
result = 0
isMinus = False

s += '+'
for i in s:
    if isMinus:
        if i == '-' or i == '+':
            result -= int(buffer)
            buffer = '0'
        else:
            '''문자열 합치기'''
            buffer += i
    else:
        if i == '-' or i == '+':
            result += int(buffer)
            buffer = '0'
            if i == '-':
                isMinus = True
        else:
            '''문자열 합치기'''
            buffer += i

print(result)
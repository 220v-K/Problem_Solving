def solution(s):
    s = list(s)
    cnt = 0
    for k in s:
        if k == "(":
            cnt += 1
        else:
            cnt -= 1
            
        if cnt < 0:
            return False
    
    if cnt != 0:
        return False
    
    return True
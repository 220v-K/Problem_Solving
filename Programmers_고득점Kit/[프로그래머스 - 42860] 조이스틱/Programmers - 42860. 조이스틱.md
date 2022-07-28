# Programmers - 42860. 조이스틱

## 접근

알파벳을 변경하기 위해 조이스틱 움직이는 횟수는 아스키코드 이용해서 처리해주면 되니 간단하다.ㅏ

문제는 커서를 이동하기 위해 움직이는 횟수.

이걸 구해내기 위한 과정이.. 대체 어디가 Greedy인지는 잘 모르겠어서 화남



```python
def solution(name):
    start = "A" * len(name)
    answer = 0

    indexToChange = []
    for i in range(len(name)):
        if name[i] != start[i]:
            indexToChange.append(i)
            
    if len(indexToChange) == 0:
        return 0

    # 각 알파벳당 조이스틱 조작 횟수
    for i in indexToChange:
        change1 = ord(name[i]) - ord("A")
        change2 = ord("Z") - ord(name[i]) + 1
        answer += min(change1, change2)

    # 커서 이동을 위한 조이스틱 조작 횟수
    if len(indexToChange) == 1:
        if 0 in indexToChange:
            answer = answer
        else:
            answer += min(indexToChange[0], len(name)-indexToChange[0])
    else:
        cursor1 = indexToChange[-1]                 # 마지막 값이 최댓값
        if 0 in indexToChange:
            cursor2 = len(name) - indexToChange[1]      # 두번째 값이 0을 제외한 최솟값
        else:
            cursor2 = len(name) - indexToChange[0]
        cursor = [cursor1, cursor2]

        for i in range(len(indexToChange)-1):
            if indexToChange[i] <= len(name) - indexToChange[i+1]:
                cursor.append(len(name)-(indexToChange[i+1]-indexToChange[i]-1))
            else:
                cursor.append(len(name)-(indexToChange[i+1]-indexToChange[i]-1)+1)
        answer += min(cursor)
        
    return answer
```



하다가 때려쳤음.

문제 쓰레기같아.
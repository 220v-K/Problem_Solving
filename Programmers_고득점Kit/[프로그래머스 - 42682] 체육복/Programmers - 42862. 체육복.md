# Programmers - 42862. 체육복

## 접근

가장 주의할 점은, 

- 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

이 조건.



도난당했으나 여벌 체육복이 있는 학생(`lost`, `reserve` 배열에 모두 포함되는 학생)은 미리 빼 줄 필요가 있음.

그 이후는 lost를 순회하며 reserve에 +1 or -1 학생이 존재하는 지(앞뒤에 여벌 체육복을 가진 학생이 존재하는 지)만 확인.

확인할 때, 오름차순으로 순회할 거면 index가 -1인 학생(앞에 있는 학생)부터 체육복이 있는 지 조사하고,

내림차순으로 순회할 때는 반대로 index가 +1인 학생(뒤에 있는 학생)부터 조사해야 함.



```python
def solution(n, lost, reserve):
    sumOfLost = 0
    lost.sort()
    templost = lost[:]

    for student in templost:
        if student in reserve:
            reserve.remove(student)
            lost.remove(student)

    templost = lost[:]
    for student in templost:
        print(student)
        if student-1 in reserve:
            reserve.remove(student-1)
            lost.remove(student)
        elif student+1 in reserve:
            reserve.remove(student+1)
            lost.remove(student)
            
    return n - len(lost)
```


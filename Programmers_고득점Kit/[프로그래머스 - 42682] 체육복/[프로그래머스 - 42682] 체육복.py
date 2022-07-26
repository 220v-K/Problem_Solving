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

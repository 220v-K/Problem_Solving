def solution(s):
    result = ""
    p = 0

    for i, c in enumerate(list(s)):
        if ord(c) < 58:
            result += c
            continue

        if p > 0:
            p -= 1
            continue

        if c == "z":
            result += "0"
            p = 3
        elif c == "o":
            result += "1"
            p = 2
        elif c == "t":
            if s[i+1] == "w":
                result += "2"
                p = 2
            else:
                result += "3"
                p = 4
        elif c == "f":
            if s[i+1] == "o":
                result += "4"
                p = 3
            else:
                result += "5"
                p = 3
        elif c == "s":
            if s[i+1] == "i":
                result += "6"
                p = 2
            else:
                result += "7"
                p = 4
        elif c == "e":
            result += "8"
            p = 4
        elif c == "n":
            result += "9"
            p = 3

    return int(result)
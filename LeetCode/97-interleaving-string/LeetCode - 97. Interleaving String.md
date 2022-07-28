# LeetCode - 97. Interleaving String

## 접근1 - 실패 (DP, List 이용)

> 일단 Topic을 보니.. DP가 들어있었는데.. DP 너무 어려워 ㅠ



s3를 순회하며 s1과 s2 두 쪽 모두에 있는 알파벳을 맞닥뜨렸을 때 처리하는 게 관건일 듯.

```python
s1 = "aabbc"
s2 = "abbcd"
s3 = "aababbbccd"
```

잘 생각이 안 나서, discuss 쪽을 살짝 들여다봤음.

https://leetcode.com/problems/interleaving-string/discuss/32076/Simple-Python-DP-solution 이거.



이런 경우, s3의 첫 index부터 s1에서 빼올지 s2에서 빼올지..

두 경우 모두를 선택하여 모두 따져봐야 함.



s3의 모든 문자를 순회하면서, s1과 s2의 현재 진행 위치를 저장하며 가면 될 듯.

`|n - m| <= 1` 조건은.. 조건 성립이 되지 않을 수가 없으므로 패스.

`s1, s2의 길이 합 != s3의 길이` 면 안되므로 예외처리.



```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        leng1 = len(s1)
        leng2 = len(s2)
        if leng1 + leng2 != len(s3):
            return False

        cursor = [[0, 0]]
        for s3char in s3:
            cursorList = []

            for n, m in cursor:
                if n < leng1 and s1[n] == s3char:
                    cursorList.append([n+1, m])
                if m < leng2 and s2[m] == s3char:
                    cursorList.append([n, m+1])

            cursor = cursorList

        if [leng1, leng2] in cursor:
            return True
        else:
            return False
```

그리고.. 시간초과.



## 접근 2 - 성공 (DP, set 이용)

시간초과... 고치려면 뭘 해야할까..

리스트를 사용했다 해도 최대 index가 2까지밖에 되지 않기 때문에, 별 상관 없을 것 같았는데 아니였다.

set을 사용하면 시간초과가 해결되었음.

근데 이러면 https://leetcode.com/problems/interleaving-string/discuss/32076/Simple-Python-DP-solution

얘랑 코드가 똑같아지는데

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        leng1 = len(s1)
        leng2 = len(s2)
        if leng1 + leng2 != len(s3):
            return False

        cursor = set([(0, 0)])
        for s3char in s3:
            cursorList = set()
            isS1 = False
            isS2 = False

            for n, m in cursor:
                if n < leng1 and s1[n] == s3char:
                    cursorList.add((n+1, m))
                    isS1 = True
                if m < leng2 and s2[m] == s3char:
                    cursorList.add((n, m+1))
                    isS2 = True
            if not cursorList:
                return False

            cursor = cursorList

        return True
```



이미 이렇게 짠 이상, DFS로 푸는 해법도 같이 보고 갈래요



- 재귀(DFS) / DP로 푼 해법

https://leetcode.com/problems/interleaving-string/discuss/2249509/Python-Simple-Solution-w-Explanation-or-Recursion-greater-DP




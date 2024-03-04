# [LeetCode/릿코드] 948. Bag of Tokens - Python

**[Medium]**



https://leetcode.com/problems/bag-of-tokens/



## 풀이

`tokens` 배열을 오름차순 정렬해준 후, Two Pointer 기법을 이용해 풀어주면 쉽게 풀이할 수 있다.



`curl`, `curr` 이라는 두 개의 커서를 각각 0, `len(tokens)` 로 초기화한 뒤, 차례로 진행해주면 된다.

현재 power가 왼쪽 커서(curl)의 토큰값보다 크다면 power를 낮추고 score를 올린 뒤(Face-up), 커서를 오른쪽으로 한 칸 이동.

현재 power가 왼쪽 커서(curl)의 토큰값보다 작다면, score가 1 이상이며, 왼쪽 커서와 오른쪽 커서가 같은 곳을 가리키지 않을 때, score를 낮추고 power를 올린다. (Face-down)

> 왼쪽 커서와 오른쪽 커서가 같은 곳을 가리킨다면, Face-down 이후 score를 올릴 token이 남지 않기 때문에, Face-down을 할 필요가 없다. (이미 오름차순 정렬을 했기 때문이다.)

두 if문 모두를 충족하지 않는다면, 게임을 할 필요가 없는 토큰들만 남은 것이므로, 게임을 종료한다.



AC.

```python
def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
    tokens = list(sorted(tokens))
    score = 0

    curl = 0
    curr = len(tokens)-1

    while curl <= curr:
        if power >= tokens[curl]:
            power -= tokens[curl]
            score += 1
            curl += 1
        elif curl+1 < curr and score > 0:
            power += tokens[curr]
            score -= 1
            curr -= 1
        else:
            break

    return score
```


# LeetCode - 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts



## 접근 - 1

가로, 세로의 잘린 간격을 리스트에 담아 저장.

가로, 세로의 간격 리스트를 이중for문으로 순회하며 곱해서 최대의 넓이를 구해냄.

```python
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizonGap = []
        verticalGap = []
        maxCuttedArea = 0

        # horizonGap, verticalGap 리스트에 잘린 간격의 칸 수를 순서대로 삽입.
        horizonGap.append(horizontalCuts[0])
        for num1, num2 in zip(horizontalCuts, horizontalCuts[1:]):
            horizonGap.append(num2 - num1)
        horizonGap.append(h - horizontalCuts[-1])

        verticalGap.append(verticalCuts[0])
        for num1, num2 in zip(verticalCuts, verticalCuts[1:]):
            verticalGap.append(num2 - num1)
        verticalGap.append(w - verticalCuts[-1])

        for ver in verticalGap:
            for hor in horizonGap:
                area = ver * hor
                if area > maxCuttedArea:
                    maxCuttedArea = area

        return (maxCuttedArea % 1000000007) 
```

> 시간초과 뜸.



## 접근 - 2

곰곰이 생각하다 깨달았음.

그냥 `horizontalGap` 과 `verticalGap` 의 최댓값만 서로 곱해주면 그게 최댓값이잖아?

```python
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxHorizonGap = 0
        maxVerticalGap = 0
        maxCuttedArea = 0

        # 가로, 세로 잘린 칸 수의 최댓값을 서로 곱함
        maxHorizonGap = horizontalCuts[0]
        for num1, num2 in zip(horizontalCuts, horizontalCuts[1:]):
            gap = num2 - num1
            if(maxHorizonGap < gap):
                maxHorizonGap = gap
        if(maxHorizonGap < (h - horizontalCuts[-1])):
            maxHorizonGap = h - horizontalCuts[-1]

        maxVerticalGap = verticalCuts[0]
        for num1, num2 in zip(verticalCuts, verticalCuts[1:]):
            gap = num2 - num1
            if(maxVerticalGap < gap):
                maxVerticalGap = gap
        if(maxVerticalGap < (w - verticalCuts[-1])):
            maxVerticalGap = w - verticalCuts[-1]

        return (maxVerticalGap * maxHorizonGap) % 1000000007
```



## 복잡도

접근 1에서는

- 시간복잡도 O(n<sup>2</sup>)
- 공간복잡도 O(n)



접근 2에서는

- 시간복잡도 O(n)
- 공간복잡도 O(1)
  - 입력되는 리스트의 크기를 고려한다면 O(n)

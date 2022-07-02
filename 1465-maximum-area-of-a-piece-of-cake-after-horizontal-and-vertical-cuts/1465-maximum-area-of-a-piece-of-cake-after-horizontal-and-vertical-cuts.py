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
# LeetCode - 376. Wiggle Subsequence



## 접근

일단 *wiggle sequence* 를 판정하는 건 어렵지 않다.

index 순서로 순회하며 두 값의 차이가 +, -, +, - 를 반복하는 지 확인하면 됨.

\+ 다음 - 가 오지 않으면 다음 인덱스로 넘어가서 다시 비교 비교 또 비교

그렇게.. 최대 길이를 구하면 될 듯

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pre_gap = 0
        now_gap = 0
        count_length_sub = 1
        if len(nums) != 1:
            for num1, num2 in zip(nums, nums[1:]):
                now_gap = num2 - num1
                wiggle = now_gap * pre_gap

                if wiggle < 0:    # now_gap, pre_gap의 부호 반대
                    count_length_sub += 1
                    pre_gap = now_gap   # wiggle 했을 때만 pre_gap의 값 변경
                if pre_gap == 0 and now_gap != 0:
                    count_length_sub += 1
                    pre_gap = now_gap   # 맨 첫번째 경우
        else:
            count_length_sub = 1

        return(count_length_sub)
```

이제 `if pre_gap == 0 and now_gap != 0:` 쪽 같은 경우는,

맨 첫 번째 경우와, 시작부터 gap이 0인 경우를 예외처리하였다.

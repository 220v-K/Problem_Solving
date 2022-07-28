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

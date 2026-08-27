class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_cnt = []
        for num in nums:
            cnt = 0
            for sub_num in nums:
                if num > sub_num:
                    cnt += 1
            max_cnt.append(cnt)
        return max_cnt

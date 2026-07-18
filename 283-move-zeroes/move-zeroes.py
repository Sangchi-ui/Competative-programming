class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c = 0
        for n in range(len(nums)):
            if nums[n] != 0:
                nums[c], nums[n] = nums[n], nums[c]
                c += 1
        return nums
        
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
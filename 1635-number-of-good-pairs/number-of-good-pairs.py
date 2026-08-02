class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i = 0
        gud_pairs = 0
        n = len(nums)
        while i < n:
           j = i + 1
           while j < n:
               if nums[i] == nums[j] and i < j:
                   gud_pairs += 1
               j += 1
           i += 1
        return gud_pairs
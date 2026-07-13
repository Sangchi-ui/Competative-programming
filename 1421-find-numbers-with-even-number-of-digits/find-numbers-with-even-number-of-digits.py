class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            s = len(str(i))
            if s%2 == 0:
                c += 1
        return c
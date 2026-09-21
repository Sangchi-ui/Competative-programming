class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        exists = []
        for num in nums1:
            if num in nums2:
                if num in exists:
                    nums2.remove(num)
                else:
                    exists.append(num)
                    nums2.remove(num)
        return exists


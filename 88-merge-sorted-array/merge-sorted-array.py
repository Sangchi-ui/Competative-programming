class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        valid1 = nums1[:m]
        valid2 = nums2[:n]
        mixed = valid1 + valid2
        mixed.sort()
        nums1[:] = mixed
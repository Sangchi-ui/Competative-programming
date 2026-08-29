class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search time
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i
            
            # Boundaries for nums1
            max_left1 = float('-inf') if i == 0 else nums1[i - 1]
            min_right1 = float('inf') if i == m else nums1[i]
            
            # Boundaries for nums2
            max_left2 = float('-inf') if j == 0 else nums2[j - 1]
            min_right2 = float('inf') if j == n else nums2[j]
            
            # Check if partition is correct
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If total elements is odd
                if (m + n) % 2 != 0:
                    return float(max(max_left1, max_left2))
                # If total elements is even
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                
            elif max_left1 > min_right2:
                high = i - 1
            else:
                low = i + 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        ones_count = n.bit_count()
        return ones_count 
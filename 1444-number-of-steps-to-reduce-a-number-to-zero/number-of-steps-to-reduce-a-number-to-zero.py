class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        remainder = num
        while remainder != 0:
            if remainder%2 == 0:
                remainder //= 2
                cnt += 1
            else:
                remainder -= 1
                remainder //= 2
                cnt += 1 if remainder == 0 else 2
        return cnt
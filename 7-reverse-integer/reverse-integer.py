class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        reversed_integer = int(str(abs(x))[::-1])
        if is_negative:
            reversed_integer = -reversed_integer 
        if reversed_integer < -2**31 or reversed_integer > 2**31 -1 :
            return 0
        return reversed_integer

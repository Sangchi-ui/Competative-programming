class Solution:
    def numDecodings(self, s: str) -> int:
        # If the string is empty or starts with '0', it cannot be decoded.
        if not s or s[0] == '0':
            return 0
        
        # prev2 represents dp[i-2] (ways to decode up to 2 steps back)
        # prev1 represents dp[i-1] (ways to decode up to 1 step back)
        prev2 = 1
        prev1 = 1
        
        for i in range(1, len(s)):
            current = 0
            
            # 1. Single digit decode (if the current character is not '0')
            if s[i] != '0':
                current += prev1
                
            # 2. Two digit decode (if the last two characters form a number between 10 and 26)
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            # Move forward for the next iteration
            prev2 = prev1
            prev1 = current
            
        return prev1
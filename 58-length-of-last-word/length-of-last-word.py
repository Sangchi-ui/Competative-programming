class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strg = s.split()
        if not strg:
            return 0
        return len(strg[-1])
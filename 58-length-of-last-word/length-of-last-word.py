class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strg = s.split()
        return len(strg[-1])
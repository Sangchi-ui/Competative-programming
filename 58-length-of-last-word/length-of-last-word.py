class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        lastwrd = len(words[-1])
        return lastwrd
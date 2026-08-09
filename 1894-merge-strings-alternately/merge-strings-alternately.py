class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        added = []
        len1, len2 = len(word1), len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                added.append(word1[i])
            if i < len2:
                added.append(word2[i])
        
        return "".join(added)
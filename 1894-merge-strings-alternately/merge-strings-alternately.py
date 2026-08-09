class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        added = []
        ranz = max(len(word1), len(word2)) 
        while i < ranz:
            if i < len(word1):
                added.append(word1[i])
            if i < len(word2):
                added.append(word2[i])
            i += 1

        return "".join(added)
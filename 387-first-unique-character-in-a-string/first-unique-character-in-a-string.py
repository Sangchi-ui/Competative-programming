class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for index, word in enumerate(s):
            if count[word]==1:
                return index
        return -1
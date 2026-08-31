from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = [0] * 26
        for ch in words[0]:
            common[ord(ch) - ord('a')] += 1

        for word in words[1:]:
            current = [0] * 26
            for ch in word:
                current[ord(ch) - ord('a')] += 1
            for i in range(26):
                common[i] = min(common[i], current[i])

        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * common[i])
        return result
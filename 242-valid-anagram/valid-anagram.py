class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for key in s:
            count[key] = count.get(key, 0) + 1
        for key in t:
            if key not in count or count[key] == 0:
                return False
            count[key] -= 1
        return True
class Solution(object):
    def isAnagram(self, s, t):
        s1 = list(s)
        s2 = list(t)
        s1.sort()
        s2.sort()
        if s1 == s2:
            return True
        else:
            return False
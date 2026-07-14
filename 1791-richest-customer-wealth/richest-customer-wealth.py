class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        add = []
        for i in accounts:
            a = 0
            for j in i:
                a += j
            add.append(a)
        return max(add)
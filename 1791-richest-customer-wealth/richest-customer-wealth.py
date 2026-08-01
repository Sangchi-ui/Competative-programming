class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(
            sum(bank_balance)
            for bank_balance in accounts
        )
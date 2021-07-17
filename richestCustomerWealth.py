# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if not accounts:
            return 0
        a = float("-inf")
        for i in accounts:
            a = max(a, sum(i))
        return a

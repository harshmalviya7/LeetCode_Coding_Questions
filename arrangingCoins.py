# 441. Arranging Coins
# https://leetcode.com/problems/arranging-coins/
class Solution:
    def arrangeCoins(self, n: int) -> int:

        i = 0
        while (n > 0):
            i += 1
            n -= i
        if n == 0:
            return i
        return i - 1

# 1561. Maximum Number of Coins You Can Get
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        sum = 0
        j = 1
        for i in range(len(piles) // 3):
            sum += piles[j]
            j += 2
        return sum

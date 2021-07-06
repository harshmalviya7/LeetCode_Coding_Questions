
# 453. Minimum Moves to Equal Array Elements
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
class Solution:
    def minMoves(self, nums: List[int]) -> int:

        n = min(nums)
        m = nums.index(n)
        res = 0
        for i in range(len(nums)):
            if i == m:
                continue
            else:
                res += nums[i] - nums[m]
        return res

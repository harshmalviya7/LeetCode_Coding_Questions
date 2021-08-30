# 747. Largest Number At Least Twice of Others
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        n = sorted(nums)
        if n[-1] >= n[-2] * 2:
            return nums.index(n[-1])
        else:
            return -1
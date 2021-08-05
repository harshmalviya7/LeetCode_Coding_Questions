# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = [1] * len(nums)
        m = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and l[i] <= l[j] + 1:
                    l[i] = 1 + l[j]

            m = max(m, l[i])

        return m

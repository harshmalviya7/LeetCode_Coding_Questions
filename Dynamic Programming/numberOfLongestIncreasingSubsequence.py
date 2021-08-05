# 673. Number of Longest Increasing Subsequence
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        l = [1] * n
        c = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if l[j] + 1 > l[i]:
                        l[i] = l[j] + 1
                        c[i] = c[j]
                    elif l[j] + 1 == l[i]:
                        c[i] += c[j]
        maxx = max(l)
        res = 0
        for i in range(len(l)):
            if l[i] == maxx:
                res += c[i]
        return res
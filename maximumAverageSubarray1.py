
# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        m = a = sum(nums[:k])

        for i in range(k, len(nums)):
            a = a - nums[i - k] + nums[i]
            if a > m:
                m = a
        return (m / k)

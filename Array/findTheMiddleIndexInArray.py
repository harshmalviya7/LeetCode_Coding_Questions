# 1991. Find the Middle Index in Array
# https://leetcode.com/problems/find-the-middle-index-in-array/
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        p = sum(nums)
        leftsum = 0
        for i in range(0, len(nums)):
            p -= nums[i]
            if p == leftsum:
                return i
            leftsum += nums[i]
        return -1

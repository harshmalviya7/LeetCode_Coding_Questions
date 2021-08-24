# 1827. Minimum Operations to Make the Array Increasing
# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        m=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                value=nums[i-1]-nums[i]+1
                nums[i]+=value
                m+=value
        return m